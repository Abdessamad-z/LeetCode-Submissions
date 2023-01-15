class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        if x==0:
            return True
        num_list=[]
        for i in range(int(math.log10(x)),-1,-1):
            y=x//10**i
            num_list.append(y)
            x-=y*10**i
        return num_list==num_list[::-1]