class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ret=[]
        i=0
        start=newInterval[0]
        end=newInterval[1]
        while i< len(intervals) and newInterval[0]>intervals[i][1]:
            ret.append(intervals[i])
            i+=1
        if i< len(intervals):
            start=min(intervals[i][0],newInterval[0])
        while i< len(intervals) and newInterval[1]>=intervals[i][0]:
            i+=1
        if i <=len(intervals) and i>0:
            end=max(intervals[i-1][1],newInterval[1])
        ret.append([start,end])
        while i<len(intervals):
            ret.append(intervals[i])
            i+=1
        return ret

