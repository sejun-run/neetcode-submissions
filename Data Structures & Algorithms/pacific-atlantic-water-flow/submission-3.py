class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rn=len(heights)
        cn=len(heights[0])
        pacific=[[False for _ in range(cn)] for _ in range(rn)]
        atlantic=[[False for _ in range(cn)] for _ in range(rn)]
        def flow(r: int,c: int, sea: List[List[int]]) -> None:
            if sea[r][c]:
                return 
            sea[r][c]=True
            for dr,dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                nr,nc=r+dr,c+dc
                if 0<=nr<rn and 0<=nc<cn and heights[nr][nc]>=heights[r][c]:
                    flow(nr,nc,sea)
        for r in range(rn):
            flow(r,0,pacific)
            flow(r,cn-1,atlantic)
        for c in range(cn):
            flow(0,c,pacific)
            flow(rn-1,c,atlantic)
        ret=[]
        for r in range(rn):
            for c in range(cn):
                if pacific[r][c] and atlantic[r][c]:
                    ret.append([r,c])
        return ret

            