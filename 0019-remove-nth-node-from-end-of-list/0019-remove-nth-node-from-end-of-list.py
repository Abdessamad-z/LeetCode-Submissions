class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next is None:
            return None
        p1,p2=head,head
        for _ in range(n):
            p2=p2.next
        if p2==None:
            return head.next
        while p2.next is not None:
            p1=p1.next
            p2=p2.next
        p1.next=p1.next.next
        return head
    