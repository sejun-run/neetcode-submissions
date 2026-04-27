class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        comb=set()
        m=1
        while m < len(nums)-1:  
            l,r=m-1,m+1
            while 0<=l and r<len(nums):
                if nums[l]+nums[m]+nums[r]>0:
                    l-=1
                elif nums[l]+nums[m]+nums[r]<0:
                    r+=1
                else:
                    comb.add((nums[l],nums[m],nums[r]))
                    l-=1
                    r+=1
            m+=1
        return [[n for n in c] for c in comb]