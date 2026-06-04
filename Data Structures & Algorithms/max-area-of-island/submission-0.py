class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        visit=set()
        marea=0
        def dfs(r,c):
            visit.add((r,c))
            area=0
            if grid[r][c]:
                area=1
                for dr,dc in [(-1,0),(1,0),(0,1),(0,-1)]:
                    nr,nc=r+dr,c+dc
                    if 0<=nr<n and 0<=nc<m and (nr,nc) not in visit:
                        area+=dfs(nr,nc)
            return area
        for r in range(n):
            for c in range(m):
                if (r,c) not in visit:
                    marea=max(marea,dfs(r,c))
        return marea
