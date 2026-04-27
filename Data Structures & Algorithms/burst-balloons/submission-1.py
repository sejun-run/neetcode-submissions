class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        cache={}
        def coins(ns):
            if tuple(ns) in cache:
                return cache[tuple(ns)]
            res=0
            for i in range(len(ns)):
                l=ns[i-1] if i!=0 else 1
                r=ns[i+1] if i!=len(ns)-1 else 1
                score=l*r*ns[i]
                newns=ns.copy()
                del newns[i]
                res=max(res,score+coins(newns))
            cache[tuple(ns)]=res
            return res
        return coins(nums)