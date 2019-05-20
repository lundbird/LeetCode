from LinkedList import LinkedList

class stack:
    def __init__(self):
        self.head = LinkedList()
    def push(self, data):
        self.head.add_first(data)
    def pop(self):
        return self.head.delete_first()
    def peek(self):
        return self.head.get(0)
    def isEmpty(self):
        return self.head.is_empty()

class queue:
    def __init__(self):
        self.head = LinkedList()
    def push(self, data):
        self.head.add_last(data)
    def pop(self):
        return self.head.delete_first()
    def peek(self):
        return self.head.get(0)
    def isEmpty(self):
        return self.head.is_empty()

if __name__=="__main__":
    test = stack()
    for i in range(4):
        test.push(i)
        print(test.peek())
    for i in range(4):
        print(test.pop())

    print()
    test = queue()
    for i in range(4):
        test.push(i)
        print(test.peek())
    for i in range(4):
        print(test.pop())

    
    