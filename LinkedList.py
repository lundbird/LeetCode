class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self, data=None):
        self.head = Node(data)
        self.size = 1

    def add_first(self, data):
        new_node = Node(data, self.head)
        self.head = new_node
        self.size += 1

    def delete_first(self):
        if (self.size < 1):
            raise ArgumentException("LinkedList has no size")
        data = self.head.data
        self.head = self.head.next
        self.size -= 1
        return data

    def add_last(self, data):
        if (self.size == 1):
            self.add_first(data)
        else:
            self.insert(data, self.size-1)

    def insert(self, data, index):
        self.__check_size(index)
        tmp = self.head
        for i in range(index-1):
            tmp = tmp.next
        new_node = Node(data, tmp.next)
        tmp.next = new_node
        self.size += 1

    def delete(self, index):
        self.__check_size(index)
        tmp = self.head
        for i in range(index-1):
            tmp = tmp.next
        data = tmp.next.data
        tmp.next = tmp.next.next
        self.size -= 1
        return data

    def delete_value(self, data):
        #feel like i should be able to refactor this mess
        tmp = self.head
        prev = tmp
        list_size = self.size
        for i in range(self.size):
            if tmp.data == data:
                if (tmp == self.head):
                    data = self.head.data
                    self.head = self.head.next
                prev.next = tmp.next
                self.size -= 1
            else:
                prev = tmp
            tmp = tmp.next

    def get(self, index):
        tmp = self.head
        for i in range(index):
            tmp = tmp.next
        return tmp.data

    def is_empty(self, index):
        return self.head is None

    def size(self):
        return self.size

    def contains(self, data):
        tmp = self.head
        for i in range(self.size):
            if tmp.data == data:
                return True
        return False

    def clear(self):
        self.head = None

    def print(self):
        tmp = self.head
        for i in range(self.size-1):
            print(tmp.data, end=' ')
            tmp = tmp.next
        print()

    def __check_size(self, index):
        if index > self.size:
            raise ValueError("invalid index")


if __name__ == "__main__":
    test = LinkedList()
    for i in range(4):
        test.add_last(i)
    test.print()
    test.insert(5, 1)
    test.print()
    test.add_last(6)
    test.print()
    print(test.contains(5))
    print(test.get(1))
    test.delete(2)
    test.print()
    test.delete_value(5)
    test.print()
    test.insert(5, 1)
    test.insert(5, 1)
    test.print()
    test.delete_value(5)
    test.print()
