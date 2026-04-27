class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r=0,len(heights)-1
        max = 0
        while l<r:
            if heights[l]<heights[r]:
                if max < (r-l)*heights[l]:
                    max=(r-l)*heights[l]
                i=1
                while heights[l]>= heights[l+i] and l+i <r:
                    i+=1
                l=l+i
            else:
                if max < (r-l)*heights[r]:
                    max=(r-l)*heights[r]
                i=1
                while heights[r]>= heights[r-i] and l <r-i:
                    i+=1
                r=r-i
        return max