class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        k=len(matrix)
        j=0
        while j<k-1-j:
            keep=matrix[j][j:k-j].copy()
            for i in range(j,k-j):
                matrix[j][k-j-i-1]=matrix[i][j]
            # print("\n".join([','.join(map(str,row)) for row in matrix]))
            for i in range(j,k-j):
                matrix[i][j]=matrix[k-j-1][i]
            for i in range(j,k-j):
                matrix[k-j-1][i]=matrix[k-j-i-1][k-j-1]
            for i in range(j,k-j):
                matrix[i][k-j-1]=keep[i-j]
            j+=1

