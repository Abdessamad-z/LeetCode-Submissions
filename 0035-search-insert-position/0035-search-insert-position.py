class Solution:
    def binary_search_rec(self,l,low,high,value):
        temp=low+math.ceil((high-low)/2)-1
        if not l[low:high]:
            return temp+1
        if l[temp]==value:
            return temp
        elif l[temp]>value:
            return self.binary_search_rec(l,low,temp,value)
        else:
            return self.binary_search_rec(l,temp+1,high,value)
    def searchInsert(self, nums: List[int], target: int) -> int:
        return self.binary_search_rec(nums,0,len(nums),target)