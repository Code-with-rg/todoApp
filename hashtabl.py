class HashTabe:
    def __init__(self, size):
        self.size = size
        self.hashtable = self.create_bucket()

    def create_bucket(self):
        return  [[] for _ in range(self.size)]
    
    def set_val(self, key, val):
        hashedkey = hash(key) % self.size
        bucket = self.hashtable[hashedkey]
        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_value = record
            
            if record_key == key :
                found_key = True
                break

        if found_key :
            bucket[index] = (key, val)
        else:
            bucket.append((key,val))

    def get_val(self, key):
        hashed_key = hash(key) % self.size
        bucket = self.hashtable[hashed_key]
        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_value = record
            if record_key == key:
                found_key = True
                break
        if found_key :
            print(f"value on {key} is {record_value}")

        else:
            print('not FOund')

    def delete_val(self, key):
        hashed_key = hash(key) % self.size
        bucket = self.hashtable[hashed_key]
        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_value = record
            if record_key == key :
                found_key = True
                break
        if found_key:
            bucket.pop(index)

    def __str__(self):
        return self.hashtable
    

hashtable = HashTabe(50)
hashtable.set_val(20,'ganesh')
hashtable.set_val(30,'Ayan')
hashtable.set_val(40,'Yashwant')
print(hashtable.__str__())
hashtable.get_val(30)
hashtable.delete_val(30)
print("===" * 20)
print(hashtable.__str__())