class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rown=len(heights)
        coln=len(heights[0])
        ret=[]
        pac=[[False for _ in range(coln)] for _ in range(rown)]
        atl=[[False for _ in range(coln)] for _ in range(rown)]
        pacpath=[]
        atlpath=[]
        def dfspac(r,c,path):
            pac[r][c]=True
            h=heights[r][c]
            path.append((r,c))
            for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                nr,nc=r+dr,c+dc
                if 0<=nr<rown and 0<=nc<coln and heights[nr][nc]>=h and (nr,nc) not in path:
                    dfspac(nr,nc,path)
        def dfsatl(r,c,path):
            atl[r][c]=True
            h=heights[r][c]
            path.append((r,c))
            for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                nr,nc=r+dr,c+dc
                if 0<=nr<rown and 0<=nc<coln and heights[nr][nc]>=h and (nr,nc) not in path:
                    dfsatl(nr,nc,path)
        for r in range(rown):
            dfspac(r,0,pacpath)
            dfsatl(r,coln-1,atlpath)
        for c in range(coln):
            dfspac(0,c,pacpath)
            dfsatl(rown-1,c,atlpath)
        for r in range(rown):
            for c in range(coln):
                if pac[r][c] and atl[r][c]:
                    ret.append([r,c])
        return ret
                    
