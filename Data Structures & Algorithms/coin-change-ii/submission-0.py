class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        clen=len(coins)
        def dfs(i,cursum):
            combs=0
            if cursum==amount:
                return 1
            if cursum>amount:
                return 0
            for l in range(i,clen):
                combs+=dfs(l,cursum+coins[l])
            return combs
        return dfs(0,0)
