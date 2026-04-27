class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        k=len(matrix)
        j=0
        while j<k-1-j:
            keep=matrix[j][j:k-j].copy()
            for i in range(j,k-j):
                matrix[j][k-1-i]=matrix[i][j]
            print("\n".join([','.join(map(str,row)) for row in matrix]),'\n')
            for i in range(j,k-j):
                matrix[i][j]=matrix[k-j-1][i]
            print("\n".join([','.join(map(str,row)) for row in matrix]),'\n')
            for i in range(j,k-j):
                matrix[k-j-1][i]=matrix[k-1-i][k-j-1]
            print("\n".join([','.join(map(str,row)) for row in matrix]),'\n')
            for i in range(j,k-j):
                matrix[i][k-j-1]=keep[i-j]
            print("\n".join([','.join(map(str,row)) for row in matrix]),'\n')
            j+=1

