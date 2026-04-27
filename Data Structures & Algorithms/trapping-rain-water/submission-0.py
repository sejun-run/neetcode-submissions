class Solution:
    def trap(self, height: List[int]) -> int:
        l,water=0,0
        while l< len(height)-2:
            while height[l]<=height[l+1] and l< len(height)-2:
                l=l+1
            r=l+2
            dark=height[l+1]
            print("left ",l)
            while r<len(height)and height[l]>height[r]:
                dark+=height[r]
                r+=1
                print("dark ",dark)
            if r!=len(height):
                water+=min(height[r],height[l])*(r-l-1)-dark
                print("right ",r,"dark ", dark, "water ", min(height[r],height[l])*(r-l-1)-dark)
            l=r
        return water 
            
