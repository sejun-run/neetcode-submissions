class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n=len(nums)
        numcnt=Counter(nums)
        freqlist=[[] for _ in range(n+1)]
        for p,v in numcnt.items():
            freqlist[v].append(p)
        returnlist=[]
        i=n
        while len(returnlist)< k:
            returnlist+=freqlist[i]
            i-=1
        return returnlist
