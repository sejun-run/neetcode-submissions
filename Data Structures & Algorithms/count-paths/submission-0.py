class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid=[[1 for _ in range(n)]for _ in range(m)]
        i=m-2
        l=n-2
        while l or i:
            for j in range(l,-1,-1):
                grid[i][j]=grid[i+1][j]+grid[i][j+1]
            for k in range(i,-1,-1):
                grid[k][l]=grid[k+1][l]+grid[k][l+1]
            if l>0:
                l-=1
            if i>0:
                i-=1
        return grid[1][0]+grid[0][1]
            