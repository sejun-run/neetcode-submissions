class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1=len(text1)
        n2=len(text2)
        subseq=[[0 for _ in range(n2+1)] for _ in range(n1+1)]
        for r in range(n1-1,-1,-1):
            for c in range(n2-1,-1,-1):
                if text1[r]==text2[c]:
                    subseq[r][c]=subseq[r+1][c+1]+1
                else:
                    subseq[r][c]=max(subseq[r+1][c],subseq[r][c+1])
        return subseq[0][0]