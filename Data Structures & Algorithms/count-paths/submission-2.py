class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ways=[[1 for _ in range(n)] for _ in range(m)]
        for row in range(m-2,-1,-1):
            for col in range(n-2,-1,-1):
                ways[row][col]=ways[row][col+1]+ways[row+1][col]
        return ways[0][0]