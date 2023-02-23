def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # move fast to nth node
        slow,fast=head,head
        for _ in range(n):
            fast=fast.next
        if not fast:
            return head.next

        #when fast gets to none, slow will be before the delete node    
        while fast.next:
            fast=fast.next
            slow=slow.next
        slow.next=slow.next.next
        return head
