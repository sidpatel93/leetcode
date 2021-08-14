# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        
        #Get the length of the linkedlist, since list is not empty(given)
        length = 1
        tail = head
        while (tail.next):
            tail = tail.next
            length+=1
            
        # print(length)
        
        # traverse the list to find the element value and adjust the decimal value at each node 
        
        decimal = 0
        tail = head
        print(tail)
        for i in reversed(range(length)):
            # print(i)
            decimal = decimal + ((tail.val)*(2**(i)))
            # print(decimal)
            tail = tail.next
            # print(tail)
        return decimal


    def second_approach(self, head):
        num = head.val
        while(head.next):
            num = num *2 + head.next.val
            head = head.next
        return num