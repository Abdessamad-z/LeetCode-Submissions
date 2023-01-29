class Solution:
    res=[]
    def rec(self,arr,target,l,index):
        for i in range(index,len(arr)):
            if arr[i]==target:
                    self.res.append(l+[arr[i]])
                    continue
            if target-arr[i]>0:
                    self.rec(arr,target-arr[i],l+[arr[i]],i)
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.res=[]
        self.rec(candidates,target,[],0)
        return self.res