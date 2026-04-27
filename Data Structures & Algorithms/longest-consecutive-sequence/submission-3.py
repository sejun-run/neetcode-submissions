class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nset=set(nums)
        start=[]
        for num in nums:
            if num-1 not in nset:
                start.append(num)
        ret=0
        for num in start:
            k=1
            while num+1 in nset:
                num+=1
                k+=1
            ret=max(ret,k)
        return ret