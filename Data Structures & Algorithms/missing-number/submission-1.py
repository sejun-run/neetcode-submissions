class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        cursum=0
        nlen=len(nums)
        for i in range(len(nums)):
            cursum+=nums[i]
        return int((nlen*(nlen+1)/2) -cursum)