class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache=[0]*(len(cost)+1)
        for i in range(2,len(cost)+1):
            res=min(cost[i-1]+cache[i-1],cost[i-2]+cache[i-2])
            cache[i]=res
        return cache[len(cost)]