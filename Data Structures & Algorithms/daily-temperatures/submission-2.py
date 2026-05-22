class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        res=[0]*len(temperatures)
        for idx, tmp in enumerate(temperatures):
            while stack and tmp> stack[-1][0]:
                for _, num in stack:
                    res[num]+=1
                stack.pop()
            stack.append([tmp,idx])
        for _,num in stack:
            res[num]=0
        return res
                
        
                
                