class Solution:
    from collections import heapq
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nmap={}
        for num in nums:
            nmap[num]=nmap.get(num,0)+1
        kelems=[]*k
        for num, freq in nmap.items():
            heapq.heappush(kelems,(freq,num))
            if len(kelems)>k:
                heapq.heappop(kelems)
        return [heapq.heappop(kelems)[1] for _ in range(k)]