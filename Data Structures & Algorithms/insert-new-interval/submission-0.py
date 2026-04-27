class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ins=newInterval[0]
        ine=newInterval[1]
        i=0
        res=[]
        flag=False
        while i <len(intervals):
            start=intervals[i][0]
            end=intervals[i][1]
            if start<=ine and ins<=end:
                news=min(start,ins)
                while intervals[i][0]<=ine:
                    i+=1
                    if i==len(intervals):
                        break
                newe = max(intervals[i-1][1],ine)
                res.append([news,newe])
            else:
                if start>=ine and not flag:
                    res.append(newInterval)
                    flag=True
                res.append(intervals[i])
                i+=1
        return res