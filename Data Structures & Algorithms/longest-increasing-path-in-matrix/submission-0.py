class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m=len(matrix)
        n=len(matrix[0])
        cache={}
        def dfs(r,c):
            if (r,c) in cache:
                return cache[(r,c)]
            res=1
            for dr,dc in [(1,0),(0,1),(-1,0),(0,-1)]:
                nr,nc=r+dr,c+dc
                if 0<=nr<m and 0<=nc<n and matrix[nr][nc]>matrix[r][c]:
                    res=max(res,dfs(nr,nc)+1)
            cache[(r,c)]=res
            return res
        long=1
        for r in range(m):
            for c in range(n):
                if (r,c) not in cache:
                    # print(r,c)
                    cur = dfs(r,c)
                    long=max(long,cur)
                    # print(cur)
        return long