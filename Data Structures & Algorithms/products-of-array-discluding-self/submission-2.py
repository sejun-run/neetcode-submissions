class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        leftsum=[1]*(n+2)
        rightsum=[1]*(n+2)
        ret=[0]*n
        for i in range(n):
            leftsum[i+1]=leftsum[i]*nums[i]
        for i in range(n+1,1,-1):
            rightsum[i-1]=rightsum[i]*nums[i-2]
        for i in range(n):
            ret[i]=leftsum[i]*rightsum[i+2]
        return ret
        
        
            