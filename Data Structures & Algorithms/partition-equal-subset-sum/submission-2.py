class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n=len(nums)
        tot=0
        for num in nums:
            tot+=num
        if tot%2:
            return False
        half=tot//2
        possible=[False]*(half+1)
        possible[0]=True
        for i in range(n-1, -1, -1):
            cur=nums[i]
            for p in range(half-nums[i],-1,-1):
                if possible[p]:
                    possible[p+nums[i]]=True
        return possible[half]