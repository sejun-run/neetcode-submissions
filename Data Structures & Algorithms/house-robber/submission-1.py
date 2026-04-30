class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        next_house=second_next=0
        for i in range(n-1,-1,-1):
            money=max(next_house, nums[i]+second_next)
            second_next=next_house
            next_house=money
        return money