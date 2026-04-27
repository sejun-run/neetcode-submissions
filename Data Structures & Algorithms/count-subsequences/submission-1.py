class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        cache=[[0 for _ in range(len(s)+1)]for _ in range(len(t)+1)]
        for j in range(len(s)+1):
            cache[len(t)][j]=1
        for i in range(len(t)-1,-1,-1):
            for j in range(len(s)-1,-1,-1):
                cache[i][j]=cache[i][j+1]
                if t[i]==s[j]:
                    cache[i][j]+=cache[i+1][j+1]
        return cache[0][0]