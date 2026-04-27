class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n=len(intervals)
        res=[]
        for i in range(len(intervals)):
            k=0
            nextres=[]
            while k<len(res) and res[k][1]<intervals[i][0]:
                nextres.append(res[k])
                k+=1
            while k<len(res) and res[k][0] <= intervals[i][1]:
                intervals[i][0]=min(intervals[i][0],res[k][0])
                intervals[i][1]=max(intervals[i][1],res[k][1])
                k+=1
            nextres.append(intervals[i])
            while k<len(res):
                nextres.append(res[k])
            res=nextres
        return res
            