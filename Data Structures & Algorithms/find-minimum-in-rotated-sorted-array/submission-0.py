class Solution:
    def findMin(self, nums: List[int]) -> int:
        s,e=0,len(nums)-1
        while s<e:
            m=(s+e)//2
            if nums[m]<nums[s]:
                e=m
            elif nums[m]>nums[e]:
                s=m+1
            else:
                return nums[s]
        return nums[s]