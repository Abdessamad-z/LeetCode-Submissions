class Solution:

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums) -1
        left = -1
        while l <= r:
            mid = (l+r) //2 
            if nums[mid] == target and (mid ==0 or nums[mid-1] != target): 
                left = mid
                break
            elif nums[mid] >= target: #recurse on left
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
        
        right = -1
        l = 0
        r = len(nums) -1
        while l <= r:
            mid = (l+r) //2 
            if nums[mid] == target and (mid == len(nums) -1 or nums[mid+1] != target): 
                right = mid
                break
            elif nums[mid] > target: #recurse on left
                r = mid - 1
            elif nums[mid] <= target: #recurse right
                l = mid + 1
                
        return [left, right]