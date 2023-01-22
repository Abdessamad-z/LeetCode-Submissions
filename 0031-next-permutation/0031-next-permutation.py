class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        if len(nums)<2:
            return
        i=-1
        while nums[i-1]>=nums[i]:
            i-=1
            if i==-len(nums):
                nums.sort()
                return
        j=i
        while nums[j]>nums[i-1] and j<0: j=j+1
        j-=1
        temp=nums[i-1]
        nums[i-1]=nums[j]
        nums[j]=temp
        nums[i:]=sorted(nums[i:])