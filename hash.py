class HashTable:
    #HashTable source: WGU C950 Webinar - 1 - Let's Go hashing ~ W-1_ ChainingHashTable_zyBooks_Key-Value.property
    #Creating the Hash Table
    def __init__(self, inital_capacity=25):
        self.table = []
        for i in range(inital_capacity):
            #Adding space for table inserts
            self.table.append([])
        
    def insert(self, key, item):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]
        #Updating value of existing key
        for keyvalue in bucket_list:
            if keyvalue[0] == key:
                keyvalue[1] = item
                return True
        
        #Inserting new item if key not found
        key_value = [key,item]
        bucket_list.append(key_value)
        return True
    
    #Search function
    def search(self,key):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]
        for each in bucket_list:
            if key == each[0]:
                return each[1]
        
        return "Key does not exist, please try again."

    #Delete function
    def delete(self,key):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]
        for each in bucket_list:
            if key == each[0]:
                bucket_list.remove(each)
        # # Testing for correct removal of key and item.
        # print(bucket_list)
        # print(bucket)

    #List all content of hash table
    def printAll(self):
        for each in range(len(self.table)):
            for package in self.table[each]:
                print(package[1].package_address)

# Testing things as needed
# if __name__ == "__main__":
#     exampleTable = HashTable()
#     exampleTable.insert(51,25)
#     print(exampleTable.search(51))
#     print("\n\n\n")
#     exampleTable.delete(51)
#     print(exampleTable.search(51))