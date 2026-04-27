class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rown=len(heights)
        coln=len(heights[0])
        ret=[]
        pathmap=[[None for _ in range(coln)] for _ in range(rown)]
        def dfs(r,c):
            if pathmap[r][c]:
                return pathmap[r][c]
            h=heights[r][c]
            pac=False
            atl=False
            if r==0 or c==0:
                pac=True
            if r==rown-1 or c == coln-1:
                atl=True
            if not pac&atl:
                for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                    nr,nc=r+dr,c+dc
                    if 0<=nr<rown and 0<=nc<coln and heights[nr][nc]<=h:
                        npac,natl=dfs(nr,nc)
                        pac=npac or pac
                        atl=natl or atl
            if pac&atl:
                ret.append((r,c))
            pathmap[r][c]=(pac,atl)
            return (pac,atl)
        for r in range(rown):
            for c in range(coln):
                dfs(r,c)
        return ret
                    
