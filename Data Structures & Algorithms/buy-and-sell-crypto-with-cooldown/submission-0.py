class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        plen=len(prices)
        buy=[0]*(plen+2)
        sell=[0]*(plen+2)
        for i in range(plen-1,-1,-1):
            buy[i]=max(buy[i+1],sell[i+1]-prices[i])
            sell[i]=max(sell[i+1],buy[i+2]+prices[i])
        return buy[0]
