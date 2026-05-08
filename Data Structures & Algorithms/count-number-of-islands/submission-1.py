class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rn=len(grid)
        cn=len(grid[0])
        def dfs(row: int, col: int) -> None:
            grid[row][col]="0"
            for dr,dc in [(-1,0),(1,0),(0,1),(0,-1)]:
                new_r,new_c=row+dr,col+dc
                if 0<=new_r<rn and 0<=new_c<cn and grid[new_r][new_c]=="1":
                    dfs(new_r,new_c)
        ret=0
        for r in range(rn):
            for c in range(cn):
                if grid[r][c]=="1":
                    ret+=1
                    dfs(r,c)
        return ret