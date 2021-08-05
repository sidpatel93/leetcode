
class Node:
    def __init__(self, value = None) -> None:
        self.value = value
        self.next = None

class SinglyLinkedlist:
    def __init__(self) -> None:
        self.head = Node()

    def append(self, data):
        newNode = Node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = newNode
    
    def length(self):
        total = 0
        cur = self.head
        while cur.next != None:
            cur = cur.next
            total = total + 1
        return total

    def insertByIndex(self, index, value):
        
        ## if the given index is outof range of the linked list then raise value error.
        if index>= self.length() and index >=0:
            print("Index is not valid")
            return 

        ## if the head is null and position is zero then insert the node at the head
        if self.head == None and index==0:
            new_node = Node(value)
            self.head = new_node
            new_node.next = None  
            return

        ## if head is not null and position is zero then insert the new node at the begining.
        if self.head != None and index ==0:
            new_node = Node()
            new_node.next = self.head.next
            self.head.next = new_node
            return
        
        ## if the head is not null and the position is non zero then insert the new node at given index.
        if self.head != None and index != 0:
            new_node = Node(value)
            cur_index = 0         
            cur_node = self.head
            last_node = None            
            while cur_index < index:
                last_node = cur_node
                cur_node = cur_node.next
                if cur_node == None:
                    break
                cur_index+=1 
            
            last_node.next = new_node
            new_node.next = cur_node
            return

    def delete():
        pass
    
    def display(self):
        elem = []
        cur = self.head
        while cur.next != None:
            cur = cur.next
            elem.append(cur.value)
        return elem


mylist = SinglyLinkedlist()
mylist.append(1)
mylist.append(5)
mylist.append(7)
print(mylist.display())
print(mylist.length())
mylist.insertByIndex(2,8)
print(mylist.display())