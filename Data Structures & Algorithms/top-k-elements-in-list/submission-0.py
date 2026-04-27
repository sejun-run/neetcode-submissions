class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numbs={}
        freq=defaultdict(list)
        for n in nums:
            numbs[n]= numbs.get(n,0)+1
        print(numbs)
        for t,v in numbs.items():
            freq[v].append(t)
        print(freq)
        sorted_freq=sorted(freq.items(),reverse=True)
        print(sorted_freq)
        ret=[]
        i=0
        while len(ret) < k :
            ret+=sorted_freq[i][1]
            i+=1
        return ret

        
