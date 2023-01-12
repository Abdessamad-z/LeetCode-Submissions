class Solution:
    def longestPalindrome(self, s):
        s=["$"]+list(s)+["@"]
        s="#".join(s)
        P=[0 for _ in s]
        c=0
        r=0
        for i in range(1,len(s)-1):
            mir=2*c-i
            if i<r:
                P[i]=min(r-i,P[mir])
            while s[i + 1 + P[i]]==s[i - 1 - P[i]]:
                P[i]+=1
            if i+P[i]>r:
                c=i
                r=i+P[i]
        index=P.index(max(P))
        s=s[index-P[index]:index+P[index]+1]
        for char in "#","@","$":
            s=s.replace(char,"")
        return s
            