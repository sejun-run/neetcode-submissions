class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n=len(nums)
        if k>n:
            return False
        window=[]
        res=[]
        for i in range(k):
            heapq.heappush(window,(-nums[i],i))
        cmax,idx=heapq.heappop(window)
        res.append(-cmax)
        heapq.heappush(window,(cmax,idx))   
        for i in range(k,n):
            heapq.heappush(window,(-nums[i],i))
            cmax,idx=heapq.heappop(window)
            while idx <= i-k:
                cmax,idx=heapq.heappop(window)
            res.append(-cmax)
            heapq.heappush(window,(cmax,idx))
        return res
        
        