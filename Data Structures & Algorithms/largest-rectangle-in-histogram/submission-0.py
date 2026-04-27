class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max=0
        for i in range(len(heights)):
            s,e = i, i
            while s>0 and heights[s-1]>= heights[i]:
                s=s-1
            while e<len(heights)-1 and heights[e+1]>= heights[i]:
                e=e+1
            area= (e-s+1)*heights[i]
            print(i,s,e,area)
            if max < area:
                max=area
        return max