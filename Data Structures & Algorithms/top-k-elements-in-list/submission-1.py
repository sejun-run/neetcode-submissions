class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numbs={}
        freq=[[]for _ in range(len(nums)+1)]
        for n in nums:
            numbs[n]= numbs.get(n,0)+1
        print(numbs)
        for t,v in numbs.items():
            freq[v].append(t)
        print(freq)
        
        ret=[]
        
        for i in range(len(freq)-1 , 0, -1):
            ret+=freq[i]
            if len(ret) == k:
                return ret

        
