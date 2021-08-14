def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        # if the linked list is empty then return the same empty list
        if not head:
            return head
        
        #find the length of the linked list
        # since we already eliminated case for empty list, the lengh would be atleast 1
        # and with 1 element linked list the head and tail point to the same node.
        length = 1
        tail = head
        # traverse through the list untill there is an element on the next.
        while tail.next:
            tail = tail.next
            length = length + 1      

        k = k % length
        
        #if the number of rotation is divisible by k then it would result in same linked list
        if k == 0:
            return head

        # traverse through the linked list to get to the break point 
        curr = head
        for i in range(length-k-1):
            curr = curr.next

        #set the new tail and the head of the linked list 
        newHead = curr.next
        curr.next = None
        
        #connect the old tail to the old head.
        tail.next = head
        
        # return the new head of the linked list
        return newHead