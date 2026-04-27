class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m=len(matrix)
        n=len(matrix[0])
        rows=[]
        cols=[]
        for r in range(m):
            for c in range(n):
                if not matrix[r][c]:
                    rows.append(r)
                    cols.append(c)
        for r in rows:
            for c in range(n):
                matrix[r][c]=0
        for c in cols:
            for r in range(m):
                matrix[r][c]=0
        
            