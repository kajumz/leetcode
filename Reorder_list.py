def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        #step 1 find middle
        if not head: return []
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        #step 2: reverse second half
        prev, curr = None, slow.next
        while curr:
            curr.next,prev,curr = prev,curr,curr.next
        slow.next = None
        
        #step 3: merge lists
        head1, head2 = head, prev
        while head2:
            nextt=head1.next
            head1.next=head2
            head1=head2
            head2=nextt
