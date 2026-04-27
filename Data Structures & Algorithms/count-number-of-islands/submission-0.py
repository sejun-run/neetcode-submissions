class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rown=len(grid)
        coln=len(grid[0])
        ret=0
        def dfs(r,c):
            grid[r][c]="0"
            for dr,dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                nr,nc = r+dr, c+dc
                if 0<=nr<rown and 0<=nc<coln and grid[nr][nc] =="1":
                    dfs(nr,nc) 

        for r in range(rown):
            for c in range(coln):
                if grid[r][c] =="1":
                    ret+=1
                    dfs(r,c)
        return ret