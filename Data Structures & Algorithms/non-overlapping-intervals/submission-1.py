class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        lastEnd=-float('inf')
        ret=0
        for start, end in intervals:
            if start < lastEnd:
                ret+=1
            else:
                lastEnd=end
        return ret