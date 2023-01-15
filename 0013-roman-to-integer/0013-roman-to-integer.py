class Solution:
    dict_num={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    def romanToInt(self, s: str) -> int:
        res=0
        last=""
        count=0
        i=0
        while i < len(s):
            char=s[i]
            i+=1
            if char in ("I","X","C") and (count==0 or char==last):
                count+=1
                last=char
                continue
            if (last=="I" and char in ("V","X")) or (last=="X" and char in ("L","C")) or (last=="C" and char in ("D","M")):
                res+=self.dict_num[char]-count*self.dict_num[last]
                count=0
                continue
            if count!=0:
                res+=count*self.dict_num[last]
                i-=1
                count=0
                continue
            res+=self.dict_num[char]
        if count!=0:
            res+=count*self.dict_num[last]
        return res