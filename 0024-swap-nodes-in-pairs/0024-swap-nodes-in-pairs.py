class Solution:
    def swapPairs(self, head):
        if head is None or head.next is None:
            return head
        temp=head.next
        head.next=self.swapPairs(temp.next)
        temp.next=head
        return temp