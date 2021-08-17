class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None
        self.pre = None

    
class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = Node()

    def append(self, value):
        newNode = Node(value)
        cur = self.head
        # Traverse to the last node in the list.
        while cur.next != None:
            cur = cur.next
        #  append the new node at the end of the last node and set the pre and next properties
        newNode.pre = cur    
        cur.next = newNode
        
    def display(self):
        elem = []
        cur = self.head
        while cur.next != None:
            cur = cur.next
            elem.append(cur.value)
        return elem


a = DoublyLinkedList()
a.append(5)
a.append(8)
print(a.display())