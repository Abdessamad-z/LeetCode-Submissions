class Solution:
    def countAndSay(self, n: int) -> str:
        if n==1:
            return "1"
        ref=self.countAndSay(n-1)
        temp=""
        count=1
        for i in range(1,len(ref)):
            if ref[i-1]==ref[i]:
                count+=1
            else:
                temp+=str(count)+ref[i-1]
                count=1
        return temp+str(count)+ref[-1]