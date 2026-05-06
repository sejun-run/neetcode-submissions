"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
            starts=[interval.start for interval in intervals]
            ends = [interval.end for interval in intervals]
            starts.sort()
            ends.sort()
            i=j=rooms=ret=0
            while i<len(starts):
                if starts[i]<ends[j]:
                    rooms+=1
                    i+=1
                    ret=max(ret,rooms)
                elif starts[i]>ends[j]:
                    rooms-=1
                    j+=1
                else:
                    i+=1
                    j+=1
            return ret