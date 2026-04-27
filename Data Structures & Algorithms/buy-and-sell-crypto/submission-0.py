class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min=prices[0]
        max=0
        for p in prices:
            if p<min:
                min=p
            elif max< p-min:
                max=p-min
            else:
                continue
        return max