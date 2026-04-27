class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            n=nums[i]
            idx=abs(n)-1
            if nums[idx]>0:
                nums[idx]*=-1
            else:
                return abs(n)
        return False
            