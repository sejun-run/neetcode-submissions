class Solution:
    def trap(self, height: List[int]) -> int:
        l,water=0,0
        while l< len(height)-2:
            while height[l]<=height[l+1] and l< len(height)-2:
                l=l+1
            r=l+2
            dark=height[l+1]
            rmax=0
            rmax_idx=r
            print("left ",l)
            while r!=len(height) and height[l]>height[r]:
                dark+=height[r]
                if rmax< height[r]:
                    rmax=height[r]
                    rmax_idx=r
                print("dark ",dark)
                print("rmax ",rmax)
                r+=1
                if r == len(height) and height[rmax_idx-1]<rmax:
                    t=rmax_idx-2
                    dark=height[rmax_idx-1]
                    while height[t]<rmax:
                        dark+=height[t]
                        t-=1
                    water+=rmax*(rmax_idx-t-1)-dark
                    print("left ",t,"dark ", dark, "water ",rmax*(rmax_idx-t-1)-dark)
                    break
            if r!=len(height):
                water+=min(height[r],height[l])*(r-l-1)-dark
                print("right ",r,"dark ", dark, "water ", min(height[r],height[l])*(r-l-1)-dark)
            l=r
        return water 
            
