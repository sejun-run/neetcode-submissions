class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        l1=len(word1)
        l2=len(word2)
        cache={}
        def dfs(i,j):
            if (i,j) in cache:
                return cache[(i,j)]
            if i>=l1:
                ret=l2-j
            elif j>=l2:
                ret=l1-i
            elif word1[i]==word2[j]:
                ret=dfs(i+1,j+1)
            else:
                deletion=dfs(i+1,j)
                insertion=dfs(i,j+1)
                replacement=dfs(i+1,j+1)
                ret=min(deletion,insertion,replacement)+1
            cache[(i,j)]=ret
            return ret
        return dfs(0,0)