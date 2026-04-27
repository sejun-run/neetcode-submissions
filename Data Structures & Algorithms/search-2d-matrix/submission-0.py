class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        s,e = 0, len(matrix)-1
        while s<e-1:
            m=(s+e)//2
            print(matrix[m][0],m,target)
            if matrix[m][0] < target:
                s=m
            elif matrix[m][0] > target:
                e=m-1
            else:
                return True
        if matrix[e][0] < target:
            t=e
        elif matrix[e][0] > target:
            t=s
        else:
            return True
        print(t)
        s, e = 1, len(matrix[0])-1
        while s<=e:
            m=(s+e)//2
            print(m)
            print(matrix[t][m],m,target)
            if matrix[t][m] < target:
                s=m+1
            elif matrix[t][m] > target:
                e=m-1
                print(s,e)
            else:
                return True
        return False