class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rown=len(heights)
        coln=len(heights[0])
        ret=[]
        pac=[[False for _ in range(coln)] for _ in range(rown)]
        atl=[[False for _ in range(coln)] for _ in range(rown)]
        def dfspac(r,c):
            pac[r][c]=True
            h=heights[r][c]
            for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                nr,nc=r+dr,c+dc
                if 0<=nr<rown and 0<=nc<coln and heights[nr][nc]>h:
                    dfspac(nr,nc)
        def dfsatl(r,c):
            atl[r][c]=True
            h=heights[r][c]
            for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                nr,nc=r+dr,c+dc
                if 0<=nr<rown and 0<=nc<coln and heights[nr][nc]>h:
                    dfsatl(nr,nc)
        for r in range(rown):
            dfspac(r,0)
            dfsatl(r,coln-1)
        for c in range(coln):
            dfspac(0,c)
            dfsatl(rown-1,c)
        for r in range(rown):
            for c in range(coln):
                if pac[r][c] and atl[r][c]:
                    ret.append([r,c])
        return ret
                    
