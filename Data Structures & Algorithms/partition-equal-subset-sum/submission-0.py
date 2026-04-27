class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2:
            return False
        half = sum(nums)//2
        n=len(nums)
        pos=[False]*(half+1)
        pos[0]=True
        for i in range(n-1,-1,-1):
            for k in range(half,-1,-1):
                pos[k]=pos[k] or pos[k-nums[i]]
        return pos[half]