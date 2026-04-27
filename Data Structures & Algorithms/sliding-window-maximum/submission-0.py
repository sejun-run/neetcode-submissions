import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ret=[]
        win=[]
        for l in range(k):
            heapq.heappush(win,[-nums[l],l])
        ret.append(-win[0][0])
        for l in range(len(nums)-k):
            heapq.heappush(win,[-nums[l+k],l+k])
            while win[0][1]<=l:
                heapq.heappop(win)
            ret.append(-win[0][0])
        return ret