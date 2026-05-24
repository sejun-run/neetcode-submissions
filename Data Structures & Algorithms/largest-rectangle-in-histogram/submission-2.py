class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n=len(heights)
        left=[0]*n
        right=[n-1]*n
        res=0
        stack=[]
        for i in range(n):
            while stack and heights[stack[-1]]> heights[i]:
                idx=stack.pop()
                right[idx]=i-1
            stack.append(i)
        stack=[]
        for i in range(n-1,-1,-1):
            while stack and heights[stack[-1]]> heights[i]:
                idx=stack.pop()
                left[idx]=i+1
            stack.append(i)
        for i in range(n):
            res=max(res,heights[i]*(right[i]-left[i]+1))
        return res
            