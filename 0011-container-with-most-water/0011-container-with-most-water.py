class Solution:
    def maxArea(self, height: List[int]) -> int:
        max=0
        i=0
        j=len(height)-1
        while(j>i):
            min=height[i] if height[i]<height[j] else height[j]
            if (j-i)*min>max:
                max=(j-i)*min
            if height[i]>height[j]:
                h=height[j]
                while h>=height[j] and j>i:
                    j-=1
            else:
                h=height[i]
                while height[i]<=h and j>i:
                    i+=1
        return max