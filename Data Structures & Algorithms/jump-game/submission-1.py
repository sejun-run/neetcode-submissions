class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i=0
        while i<len(nums):
            if i==len(nums)-1:
                return True
            if nums[i]!=0:
                i=i+nums[i]
            else:
                return False
        return True