"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x: x.end)
        left=[i for i in range(len(intervals))]
        count=0
        while left:
            nleft=[]
            curend=-1
            for i in left:
                if intervals[i].start< curend:
                    nleft.append(i)
                else:
                    curend=intervals[i].end
            left=nleft
            count +=1
        return count