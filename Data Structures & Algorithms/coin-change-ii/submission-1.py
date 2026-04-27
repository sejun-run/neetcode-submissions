class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        clen=len(coins)
        cache={}
        def dfs(i,cursum):
            combs=0
            if cursum==amount:
                return 1
            if cursum>amount:
                return 0
            if (i,cursum) in cache:
                return cache[(i,cursum)]
            for l in range(i,clen):
                combs+=dfs(l,cursum+coins[l])
            cache[(i,cursum)]=combs
            return combs
        return dfs(0,0)
