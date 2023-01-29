class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n1,n2=0,0
        for c in range(len(num1)):
            n1+=(ord(num1[c])-48)*10**(len(num1)-1-c)
        for c in range(len(num2)):
            n2+=(ord(num2[c])-48)*10**(len(num2)-1-c)
        return str(n1*n2)