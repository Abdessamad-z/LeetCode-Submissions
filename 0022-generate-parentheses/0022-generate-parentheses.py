class Solution:
    def generateParenthesis(self, n: int):
        target=[]
        def rec(l,left,right):
            if right==n:
                target.append(l)
                return
            if left<n:
                rec( l +"(", left + 1, right)
            if right<left:
                rec(l +")", left, right + 1)
        target=[]
        rec("", 0, 0)
        return target