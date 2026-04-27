class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m=len(text1)
        n=len(text2)
        lcs=[[0 for i in range(n)]for j in range(m)]
        def getlcs(r,c):
            if r==-1 or c==-1:
                return 0
            if not lcs[r][c]:
                if text1[r]==text2[c]:
                    lcs[r][c]=min(getlcs(r-1,c),getlcs(r,c-1))+1
                else :
                    lcs[r][c]=max(getlcs(r-1,c),getlcs(r,c-1))
            return lcs[r][c]
        return getlcs(m-1,n-1)
