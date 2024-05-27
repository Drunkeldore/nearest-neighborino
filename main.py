from hash import HashTable
import csv
from package import Package
  
  
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
        hashtable.insert(package_id, package)

# # Testing things
if __name__ == "__main__":
    hashtable = HashTable()
    loadPackageData(hashtable, "CSVFiles\packageCSV.csv")

