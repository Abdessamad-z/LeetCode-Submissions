class Solution:
    def lengthOfLongestSubstring(self,s):
        l=len(s)
        if l==0:
            return 0
        m=[1]*l
        for i in range(l):
            for j in range(i+1,l):
                if s[j] in s[i:j]:
                    break
                m[i]+=1
        return max(m)