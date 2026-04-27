class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        globmax=None
        prodmax=1
        prodmin=1
        for num in nums:
            prodmax=max(prodmax*num,prodmin*num,num)
            prodmin=min(prodmax*num,prodmin*num,num)
            if not globmax or globmax < prodmax:
                globmax=prodmax
        return globmax