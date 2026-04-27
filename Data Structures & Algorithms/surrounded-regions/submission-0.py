class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rown=len(board)
        coln=len(board[0])
        def dfs(r,c,path):
            path.add((r,c))
            for dr,dc in [(-1,0),(1,0),(0,1),(0,-1)]:
                nr,nc= r+dr, c+dc
                if not(0<=nr<rown and 0<=nc<coln):
                    path.add('Flag')
                    return
                if board[nr][nc]=='O' and (nr,nc) not in path:
                    dfs(nr,nc,path)

        for r in range(rown):
            for c in range(coln):
                if board[r][c]=='O':
                    print(r,c)
                    path=set()
                    dfs(r,c,path)
                    print(path)
                    if 'Flag' not in path:
                        for surr,surc in path:
                            board[surr][surc]='X'