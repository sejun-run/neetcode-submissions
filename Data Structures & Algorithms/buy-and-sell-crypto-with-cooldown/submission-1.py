class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp={}

        def dfs(i,buy):
            if i >=len(prices):
                return 0
            if (i,buy) in dp:
                return dp[(i,buy)]
            if buy:
                dp[(i,buy)]= max(dfs(i+1,True),-prices[i]+dfs(i+1,False))
            else:
                dp[(i,buy)]= max(dfs(i+1,False),prices[i]+dfs(i+2,True))
            return dp[(i,buy)]
        return dfs(0,True)