class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        few=[0]*(amount+1)
        for i in range(1,amount+1):
            fewnum=-1
            for coin in coins:
                if i-coin>=0 and few[i-coin]!=-1 and (fewnum==-1 or fewnum>few[i-coin]+1):
                    fewnum=few[i-coin]+1
            few[i]=fewnum
        return few[amount]