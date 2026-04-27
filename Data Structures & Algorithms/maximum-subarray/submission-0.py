class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        l,r=0,0
        maxsum=None
        cursum=0
        for r in range(len(nums)):
            cursum+=nums[r]
            if not maxsum or maxsum<cursum:
                maxsum=cursum
            if cursum<0:
                l=r+1
                cursum=0
        return maxsum