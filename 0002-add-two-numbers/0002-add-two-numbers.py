class Solution:
    def addTwoNumbers(self, l1, l2):
        p1=l1
        p2=l2
        s1=''
        while(l1!=None):
            s1 = str(l1.val) + s1
            l1 = l1.next
        s2=''
        while (l2 != None):
            s2 = str(l2.val) +s2
            l2 = l2.next
        if p1==None and p2==None:
            return ListNode(0)
        elif p1==None:
            s=str(int(s2))
        elif p2==None:
            s=str(int(s1))
        else:
            s=str(int(s1)+int(s2))
        c1=ListNode(int(s[0]))
        solution=c1
        for i in range(1,len(s)):
            if i%2==1:
                c2=ListNode(int(s[i]))
                c2.next=c1
                solution=c2
            else:
                c1=ListNode(int(s[i]))
                c1.next=c2
                solution=c1
        return solution