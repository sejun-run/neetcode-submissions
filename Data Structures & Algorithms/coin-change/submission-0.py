class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache=[-1]*(amount+1)
        cache[amount]=0
        for i in range(amount-1,-1,-1):
            for coin in coins:
                if coin+i < len(cache) and cache[coin+i]>=0:
                    if cache[i]>cache[coin+i]+1 or cache[i]==-1:
                        cache[i]= cache[coin+i]+1
        return cache[0]
                    

            
        
