class Solution:
    def canJump(self, nums: List[int]) -> bool:
        res=[False for _ in range(len(nums))]
        res[len(nums)-1]=True
        for i in range(len(nums)-1,-1,-1):
            for t in range(nums[i]):
                if i+t+1< len(nums) and res[i+t+1]:
                    res[i]=True
        return res[0]