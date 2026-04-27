class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map={}
        freq=[[] for _ in range(len(nums)+1)]
        for num in nums:
            map[num]=map.get(num,0)+1
        for n,f in map.items():
            freq[f].append(n)
        ret=[]
        for bucket in reversed(freq):
            if len(ret) < k:
                ret+=bucket
            else:
                return ret
        raise exception
