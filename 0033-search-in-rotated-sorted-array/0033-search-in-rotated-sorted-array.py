class Solution:
    def binary_search(self,arr, low, high, x):
        mid = (high + low) // 2
        if x==arr[mid]:
            return mid
        if low>=high:
            return -1
        if (arr[low]<=arr[mid] and arr[mid] > x >= arr[low]) or (arr[high]>arr[mid] and (x<arr[mid] or x>arr[high])) :
            return self.binary_search(arr, low, mid - 1, x)
        else:
            return self.binary_search(arr, mid + 1, high, x)
    
    def search(self, nums: List[int], target: int) -> int:
        return self.binary_search(nums, 0, len(nums)-1, target)