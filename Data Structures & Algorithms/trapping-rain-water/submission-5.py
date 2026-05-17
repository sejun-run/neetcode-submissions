class Solution:
    def trap(self, height: List[int]) -> int:
        res=0
        l=0
        r=len(height)-1
        for i in range(1,len(height)):
            if height[i]>=height[l]:
                area=(i-l-1)*height[l]
                for block in range(l+1,i):
                    area-=height[block]
                res+=area
                l=i
        for i in range(len(height)-2,l-1,-1):
            if height[i]>=height[r]:
                area=(r-i-1)*height[r]
                for block in range(i+1,r):
                    area-=height[block]
                res+=area
                r=i
        return res
                
            