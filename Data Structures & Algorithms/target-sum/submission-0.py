class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache={}
        def dfs(i,csum):
            if i==len(nums):
                if csum==target:
                    return 1
                else:
                    return 0
            if (i,csum) in cache:
                return cache[(i,csum)]
            cursum=dfs(i+1,csum-nums[i])+dfs(i+1,csum+nums[i])
            cache[(i,csum)]=cursum
            return dfs(i,csum)
        return dfs(0,0)
