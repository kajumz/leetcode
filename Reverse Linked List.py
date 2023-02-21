# iterative

def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
  cur,prev=head,None
  while cur:
    cur.next, prev, cur=prev, cur, cur.next
  return prev
