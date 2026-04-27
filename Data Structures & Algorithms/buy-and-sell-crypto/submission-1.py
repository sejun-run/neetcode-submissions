class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b,ret=0,0
        for s in range(len(prices)):
            if prices[s]<prices[b]:
                b=s
            else:
                ret= max(ret,prices[s]-prices[b])
        return ret
             