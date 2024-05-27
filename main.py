# Nick Porter
# Student ID: 011452649

from hash import HashTable
import csv
from package import Package
from truck import DeliveryTruck
import datetime
  
# FUNCTION DEFINITIONS:
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



# Creating hash table and populating with packages
hashtable = HashTable()
loadPackageData(hashtable, "CSVFiles\packageCSV.csv")

# Formatting both address and distance CSV for use
address_csv = csv_list_formatter("CSVFiles\\addressCSV.csv")
distance_csv = csv_list_formatter("CSVFiles\distanceCSV.csv")

# Creating and loading delivery trucks manually within constraints
# Trucks 1 and 2 leave right away, 3 waits for the return of whichever other truck comes first before leaving.
# Packages are roughly arranged, manually,  by time sensitivity before the algorithm sorts them by shortest distance.

del_truck_1 = DeliveryTruck(0.0, [15, 13, 14, 16, 19, 20, 1, 6, 14, 21, 29, 30, 31, 34], "4001 South 700 East", datetime.timedelta(hours=8))
del_truck_2 = DeliveryTruck(0.0, [36, 38, 6, 25, 28, 32, 37, 40, 2, 3, 4, 5, 7, 8], "4001 South 700 East", datetime.timedelta(hours=9, minutes=5))
del_truck_3 = DeliveryTruck(0.0, [9, 10, 11, 12, 17, 18, 19, 22, 23, 24, 26, 27, 33, 35, 39], "4001 South 700 East", datetime.timedelta(hours=10, minutes=20))




# # Testing things during development below
#if __name__ == "__main__":

    #testing to see if package data is loaded
    
    #Checking package and content using various methods
    # check = hashtable.search(1)
    # print(check.package_content())

