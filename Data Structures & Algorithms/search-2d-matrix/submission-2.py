class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m=len(matrix)
        n=len(matrix[0])
        l,r=0,m-1
        row=0
        while l<=r:
            m=(l+r)//2
            if matrix[m][0]<=target:
                row=m
                l=m+1
            else:
                r=m-1
        l,r=0,n-1
        while l<=r:
            m=(l+r)//2
            if matrix[row][m]==target:
                return True
            elif matrix[row][m]>target:
                r=m-1
            else:
                l=m+1
        return False