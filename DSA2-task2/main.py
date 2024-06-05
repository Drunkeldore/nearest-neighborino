# Nick Porter
# Student ID: 011452649

from hash import HashTable
import csv
from package import Package
from truck import DeliveryTruck
import datetime
  

MILES_PER_HOUR = 18
TRUCK_CAPACITY = 16
NUMBER_OF_PACKAGES = 40
# FUNCTION DEFINITIONS:_
    #function for loading package data into hash table
def loadPackageData(hashtable, csv_file):
    """Takes and inputs HashTable into CSV file"""
    with open(csv_file) as file:
        package_data = list(csv.reader(file))
   # Going through each row of the CSV and creating a package to store in the Hash table.
    for each in package_data:
        package_id = int(each[0])
        package_address = each[1]
        package_city = each[2]
        package_state = each[3]
        package_zip = each[4]
        package_deadline = each[5]
        package_weight = each[6]
        package_status = "At the hub"
        package = Package(package_id, package_address, package_city, package_state, package_zip, package_deadline, package_weight, package_status)
        # Storing each package into the hashtable
        hashtable.insert(package_id, package)

    # Function for storing contents of other CSV files
def csv_list_formatter(csv_file):
    with open(csv_file) as file:
        csv_data = list(csv.reader(file))
        return csv_data

    # Taking string address and returning corresponding index for finding distance
def address_index(address):
    for each in address_csv:
        if each[2] == address:
            return int(each[0])

    # Find the distance between two places based on the address index. 
    # Can return "" because distance from A -> B == B -> A and CSV does not duplicate values
    # Uses if statement to flip row/column.
def distance_finder(place1, place2):
    distance = distance_csv[place1][place2]
    if distance == "":
        distance = distance_csv[place2][place1]
    return float(distance) # Uses float for better accuracy within algorithm.

def maximum_distance(csv_file): # Created function for finding largest number for more precision
    """ Returns Largest Number + 1 for checking distance in Nearest Neighbor algorithm. Takes distance csv as input"""
    max = 0.0
    for row in csv_file:
        for each in row:
            if (each != "") and (float(each) > float(max)):
                max = each
    return (float(max) + 1)

#Creates unordered duplicate list of packages, orders original list by shorest distance using nearest neighbor algorithm.
#Once sorted, mileage is added to truck total
def shortest_route(truck):
    unordered_load = []
    for each in truck.packages:
        package = hashtable.search(each)
        unordered_load.append(package) #Duplicating truck load to order by shorest distance
    
    truck.packages.clear()

    # Beginning of Algorithm
    # Used Section D of Project IMplementation Steps - Example - Nearest Neighbor to help guide the process of the algorithm.
    # Looping while unordered_load still has packages
    while len(unordered_load) > 0:
        next_address = maximum_distance(distance_csv)
        next_package = None

        for each in unordered_load: #Every iteration of the while loop we loop through whats left of unordered_load to find the next shorest path
            current_address = distance_finder(address_index(truck.currentLocation), address_index(each.address))
            if  current_address <= next_address:
                next_address = current_address
                next_package = each
        
        truck.packages.append(next_package.id) # That next shorest path gets appeneded to the truck list
        unordered_load.remove(next_package) # Then is removed from the unordered_load list as it's now considered sorted.and

        # Updates mileage between current address and next shortest address to truck and updates time stamps for truck and package
        truck.currentTime += datetime.timedelta(hours = next_address / MILES_PER_HOUR) # Use global in case average speed of truck changes
        truck.miles += next_address
        truck.currentLocation = next_package.address
        next_package.deliveryTime = truck.currentTime
        next_package.deparTime = truck.initalTime


# Creating hash table and populating with packages
hashtable = HashTable()
loadPackageData(hashtable, "CSVFiles\packageCSV.csv")

# Formatting both address and distance CSV for use
address_csv = csv_list_formatter("CSVFiles\\addressCSV.csv")
distance_csv = csv_list_formatter("CSVFiles\distanceCSV.csv")
package_csv = csv_list_formatter("CSVFiles\packageCSV.csv")

# Creating and loading delivery trucks manually within constraints
# Trucks 1 and 2 leave right away, 3 waits for the return of whichever other truck comes first before leaving.
# Packages are roughly arranged, manually,  by time sensitivity before the algorithm sorts them by shortest distance.

del_truck_1 = DeliveryTruck(0.0, [15,1,13,14,16,20,29,30,31,34,37,40,19], "4001 South 700 East", datetime.timedelta(hours=8))
del_truck_2 = DeliveryTruck(0.0, [3,18,36,38,6,25,28,32,2,4,5,7,8,10], "4001 South 700 East", datetime.timedelta(hours=9, minutes=5))
del_truck_3 = DeliveryTruck(0.0, [11,12,17,21,22,23,24,26,27,33,35, 9,39], "4001 South 700 East", datetime.timedelta(hours=10,minutes=20))

shortest_route(del_truck_1)
shortest_route(del_truck_2)
shortest_route(del_truck_3)


# # Testing things during development below
if __name__ == "__main__":
    
    # Creating UI to check on package status as well as total mileage of delivery trucks
    print(f"----------------------\n"
        f"|WGU DELIVERY SERVICES|\n"
        f"----------------------\n\n\n\n")
    
    print(f"*********************************************************")
    print("1. Print total mileage of the trucks.")
    print("2. Print information of a given package at a given time.")
    print(f"3. Print all information for all packages at a given time.\n\n")

    stop = False
    while stop == False: # Looping until active is made false by user choice or program termination
        user_choice = input("What would you like to see? (Input 1, 2, 3, exit): ")

        if user_choice == str(1):
            print(f"The total distance travelled for all delivery trucks is: {del_truck_1.miles + del_truck_2.miles + del_truck_3.miles}")
    
        elif user_choice == str(2):

            # Attempting to ask for time in correct format then converting it to datetime
            try:
                user_time = input("Enter the time XX:XX:XX of a package to check it's status: \n")
                user_id = input("Please enter a package ID number: ")
                time_formatted = (user_time.split(":"))
                time_formatted = [int(each) for each in time_formatted] # Converting to integers for datetime
                time_selected = datetime.timedelta(hours=time_formatted[0], minutes=time_formatted[1], seconds=time_formatted[2])
                if time_selected >= datetime.timedelta(hours=10, minutes=20):
                        package_9 = hashtable.search(9)
                        package_9.address = "410 S State St"
                        package_9.city = "Salt Lake City"
                        package_9.state = "UT"
                        package_9.zip = "84111"
                # Searching and printing package data as well as restarting if ValueError is thrown
                selected_package = hashtable.search(int(user_id))
                selected_package.status_update(time_selected)
                print(selected_package.package_content())
            except ValueError:
                print("Not valid, restarting program")
        
        elif user_choice == str(3):
            try:
                # Very similar to checking an individual package. This choice just loops through the number of possible packages and prints their status based on what time is entered.
                user_time = input("Enter the time XX:XX:XX to check the status of all packages: \n")
                time_formatted = (user_time.split(":"))
                time_formatted = [int(each) for each in time_formatted] # Converting to integers for datetime
                time_selected = datetime.timedelta(hours=time_formatted[0], minutes=time_formatted[1], seconds=time_formatted[2])
                if time_selected >= datetime.timedelta(hours=10, minutes=20):
                    package_9 = hashtable.search(9)
                    package_9.address = "410 S State St"
                    package_9.city = "Salt Lake City"
                    package_9.state = "UT"
                    package_9.zip = "84111"

                for each in range(1, NUMBER_OF_PACKAGES + 1):
                    current_package = hashtable.search(each)
                    current_package.status_update(time_selected)
                    print(current_package.package_content())
            
            except ValueError:
                print("Not a valid entry, restarting program.")
        elif user_choice == "exit":
            stop = True
        else:
            #Checking to make sure whatever is entered is a valid choice (1,2,3,exit)
            print("Not quite a valid input, try again.")


