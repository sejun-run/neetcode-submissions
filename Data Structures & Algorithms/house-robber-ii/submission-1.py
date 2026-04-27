class Solution:
    def rob(self, nums: List[int]) -> int:
        hnum=len(nums)
        mcache=[0]*len(nums)
        scache=[0]*len(nums)
        mcache[hnum-1]=nums[hnum-1]
        scache[hnum-2]=nums[hnum-2]
        mcache[hnum-2]=max(nums[hnum-1],nums[hnum-2])
        for i in range(hnum-3,-1,-1):
            mcache[i]=max(mcache[i+1],mcache[i+2]+nums[i])
            scache[i]=max(scache[i+1],scache[i+2]+nums[i])
        if hnum>1:
            mcache[0]=mcache[1]
        print(mcache)
        return max(mcache[0],scache[0])