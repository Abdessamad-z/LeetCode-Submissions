class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        x=0
        for i in range(len(min(strs,key=len))):
            if len(set([st[i] for st in strs]))>1:
                break
            x+=1
        return strs[0][:x]
                