from LinkedList import LinkedList


class HashTable:
    def __init__(self, size=10):
        self.array = [None] * size
        for i in range(size):
            self.array[i] = LinkedList()
        # self.array = [LinkedList()] * size #will have the SAME LL for each entry lol
        self.size = size

    def insert(self, data):
        bucket = self.hash_code(data)
        # print(bucket, self.array[bucket])
        self.array[bucket].add_first(data)

    def lookup(self, data):
        bucket = self.hash_code(data)
        return self.array[bucket].contains(data)

    def delete(self, data):
        bucket = self.hash_code(data)
        return self.array[bucket].delete_value(data)

    def print(self):
        for i in range(self.size):
            self.array[i].print()

    def hash_code(self, data):
        return data % self.size



if __name__ == "__main__":
    test = HashTable()
    for i in range(15):
        test.insert(i)
        test.insert(14-i)
    test.print()
    print()
    print(test.lookup(4))
    print(test.lookup(-1))
    for i in range(10):
        test.delete(i)
    test.print()