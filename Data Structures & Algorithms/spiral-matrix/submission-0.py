class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        l=t=0
        r=len(matrix[0])
        b=len(matrix)
        ret=[]
        while True:
            if t+1==b:
                print(l,r)
                for i in range(l,r):
                    ret.append(matrix[t][i])
                return ret
            if l+1==r:
                for i in range(t,b):
                    ret.append(matrix[i][r-1])
                return ret
            for i in range(l,r-1):
                ret.append(matrix[t][i])
            for i in range(t,b-1):
                ret.append(matrix[i][r-1])
            for i in range(r-1,l,-1):
                ret.append(matrix[b-1][i])
            for i in range(b-1,t,-1):
                ret.append(matrix[i][l])
            if not (b-2>t or r-2>l):
                return ret
            if b-2>t:
                b-=1
                t+=1
            if r-2>l:
                r-=1
                l+=1

        
