class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class BST:
    def __init__(self, root=None):
        self.root = root

    def insert(self, valueToInsert):
        newNode = Node(valueToInsert)
        # if there is no root node then add the newNode as the root.
        if self.root is None:
            self.root = newNode
            return self
        # start from the root node
        # keep cheking if the value is greater or less than it's children
        current = self.root
        while(True):
            if valueToInsert == current.value:
                return None
            if valueToInsert < current.value:
                if(current.left is None):
                    current.left = newNode
                    return self
                current = current.left
            elif valueToInsert > current.value:
                if current.right is None:
                    current.right = newNode
                    return self
                current = current.right

    def find(self, valueToFind):
        if self.root is None:
            return None
        current = self.root
        result = False
        while not result and current is not None:
            if valueToFind < current.value:
                current = current.left
            elif valueToFind > current.value:
                current = current.right
            elif valueToFind == current.value:
                result = True
                return result
        return result







tree = BST()
tree.insert(10)
tree.insert(5)
tree.insert(13)
tree.insert(2)
tree.insert(16)
tree.insert(11)
tree.insert(7)

print(tree.root. value) #10
print(tree.root.left.value) #5
print(tree.root.right.value) #13
print(tree.root.left.left.value) #2
print(tree.root.right.left.value) #11

print(tree.find(13))
print(tree.find(5))
print(tree.find(15))
print(tree.find(11))
print(tree.find(16))
