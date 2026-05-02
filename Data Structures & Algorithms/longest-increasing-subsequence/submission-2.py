class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        sub=[1]*n
        ret=-float("inf")
        for i in range(n-1,-1,-1):
            for j in range(i,n):
                if nums[j]> nums[i]:
                    sub[i]=max(sub[i],sub[j]+1)
            ret=max(ret,sub[i])
        return ret