class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        maxlen=0
        nlen=len(nums)
        cache=[0]*nlen
        for i in range(nlen-1,-1,-1):
            curmax=0
            for j in range(i+1,nlen,1):
                print(j,nums[j])
                if nums[j]>nums[i]:
                    curmax=max(curmax,cache[j])
            print(curmax)
            cache[i]=curmax+1
            maxlen=max(cache[i],maxlen)
        print(cache)
        return maxlen
        
