class Solution:
    def rob(self, nums: List[int]) -> int:
        hnum=len(nums)
        cache=[0]*hnum
        cache[hnum-1]=nums[hnum-1]
        cache[hnum-2]=max(nums[hnum-1],nums[hnum-2])
        for i in range(hnum-3,-1,-1):
            cache[i]=max(cache[i+2]+nums[i],cache[i+1])
        return cache[0]