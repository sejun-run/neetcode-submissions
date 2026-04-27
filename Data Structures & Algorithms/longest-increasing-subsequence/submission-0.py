class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        maxlen=0
        nlen=len(nums)
        cache=[0]*nlen
        for i in range(nlen-1,-1,-1):
            curmax=1
            for j in range(i,nlen-1):
                if nums[j]>nums[i]:
                    curmax=max(curmax,cache[j])
            cache[i]=curmax+1
            maxlen=max(cache[i],maxlen)
        return maxlen
        
