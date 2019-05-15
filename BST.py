class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


defaultNode = TreeNode(0)
class BST:
    def __init__(self, data):
        self.root = TreeNode(data)

    def contains(self, data, node=defaultNode):
        if (node == defaultNode):
            node = self.root

        if (node == None):
            return False
        if (node.data == data):
            return True
        if (data < node.data):
            return self.contains(data, node.left)
        else:
            return self.contains(data, node.right)

    def insert(self, data, node=defaultNode):
        if (node == defaultNode):
            node = self.root
        if (node == None):
            return TreeNode(data)
        if (data < node.data):
            node.left = self.insert(data, node.left)
        elif (data > node.data):
            node.right = self.insert(data, node.right)
        else:
            pass  # do nothing on duplicate keys
        return node

    def inorder(self, node):
        if node is None:
            return
        self.inorder(node.left)
        print(node.data, end=' ')
        self.inorder(node.right)

    def postorder(self, node):
        if node is None:
            return
        self.postorder(node.left)
        self.postorder(node.right)
        print(node.data, end=' ')

    def preorder(self, node):
        if node is None:
            return
        print(node.data, end=' ')
        self.preorder(node.left)
        self.preorder(node.right)


if __name__ == "__main__":
    test = BST(4)
    test.insert(2)
    test.insert(1)
    test.insert(3)
    test.insert(6)
    test.insert(5)
    test.insert(7)
    test.inorder(test.root)
    print()
    print(test.contains(4))
    print(test.contains(1))
    print(test.contains(-1))
    test.preorder(test.root)
    print()
    test.postorder(test.root)
    print()
    test.inorder(test.root)
    print()
