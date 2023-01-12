class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1:
            return s
        output=""
        for j in range(numRows):
            if j>len(s)-1:
                break
            line=""
            c=True
            i=j
            spacing=0
            while i<len(s):
                line+=s[i]
                if j in [0,numRows-1]:
                    i+=(numRows-1)*2
                else:
                    if c==True:
                        i+=(numRows-j-1)*2
                        c=False
                    else:
                        i+=j*2
                        c=True
            output+=line
        return output