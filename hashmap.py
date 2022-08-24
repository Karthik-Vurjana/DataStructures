# implementing hashmap in python using chaining method to avoid collisions..

class HashMap:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]

    def get_hash_value(self, key):
        hash_value = 0
        for c in key:
            hash_value += ord(c)
        return hash_value % self.MAX

    def __setitem__(self, key, value):
        hash_value=self.get_hash_value(key)
        found=False
        for index, element in enumerate(self.arr[hash_value]):
            if len(element)==2 and element[0]==key:
                self.arr[hash_value][index]=(key,value)
                found=True
                break
        if not found:
            self.arr[hash_value].append((key,value))

    def __getitem__(self, item):
        hash_value=self.get_hash_value(item)
        for index,element in enumerate(self.arr[hash_value]):
            if element[0]==item:
                return element[1]

    def __delitem__(self, key):
        hash_value=self.get_hash_value(key)
        for index,element in enumerate(self.arr[hash_value]):
            if element[0]==key:
                del self.arr[hash_value][index]
                break


if __name__ == '__main__':
    hashmap = HashMap()
    hashmap["Oct 12"]="Govind"
    hashmap["Oct 19"]= "Karthik"
    hashmap["march 6"]= "Vurjana"
    hashmap["march 17"]= "Karthik"

    print(hashmap.arr)

    del hashmap["march 17"]


    print(hashmap.arr)
