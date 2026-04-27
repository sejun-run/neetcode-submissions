class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max=0
        rstack=[]
        rlist=[0 for _ in range(len(heights))]
        for i in range(len(heights)):
            while len(rstack)>0 and heights[rstack[-1]]> heights[i]:
                rlist[rstack.pop()]= i-1   
            rstack.append(i)
        for r in rstack:
            rlist[r]= len(heights)-1
        lstack=[]
        llist=[0 for _ in range(len(heights))]
        for i in range(len(heights)-1,-1,-1):
            while len(lstack)>0 and heights[lstack[-1]]> heights[i]:
                llist[lstack.pop()]= i+1   
            lstack.append(i)
        for l in lstack:
            llist[l]= 0
        print(rlist,llist)
        for i in range(len(heights)):
            s,e = llist[i], rlist[i]
            area= (e-s+1)*heights[i]
            print(i,s,e,area)
            if max < area:
                max=area
        return max