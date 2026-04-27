class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        curend=intervals[0][1]
        i=1
        count=0
        while i<len(intervals):
            while i<len(intervals) and curend > intervals[i][0]:
                count+=1
                i+=1
            if i<len(intervals):
                curend=intervals[i][1]
            i+=1
        return count