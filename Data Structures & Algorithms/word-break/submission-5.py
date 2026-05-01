class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n=len(s)
        res=[False]*(n+1)
        res[n]=True
        for i in range(n-1,-1,-1):
            for word in wordDict:
                flag=True
                for v,w in enumerate(word):
                    if i+v>=len(s) or s[i+v]!=w:
                        flag=False
                        break
                res[i]=True if flag and res[i+v+1] else res[i]
                    
        return res[0]