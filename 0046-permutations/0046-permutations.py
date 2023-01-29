class Solution:
    res=[]
    def rec(self,nums,l):
        if nums==[]:
            self.res.append(l)
            return
        for i in range(len(nums)):
            self.rec(nums[:i]+nums[i+1:],l+[nums[i]])
            
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res=[]
        self.rec(nums,[])
        return self.res