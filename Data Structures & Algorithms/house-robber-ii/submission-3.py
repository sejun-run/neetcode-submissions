class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        rob1=rob2=0
        for i,n in enumerate(nums[:-1]):
            rob1,rob2=max(n+rob2,rob1),rob1
        first=rob1
        rob1=rob2=0
        for i,n in enumerate(nums[1:]):
            rob1,rob2=max(n+rob2,rob1),rob1
        last=rob1
        return max(first,last)