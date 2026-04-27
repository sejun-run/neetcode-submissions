class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def check(path,r,c,char):
            ret=set()
            if r-1>=0 and (not (r-1,c) in path) and board[r-1][c]==char:
                ret.add((r-1,c))
            if r+1<len(board) and (not (r+1,c) in path) and board[r+1][c]==char:
                ret.add((r+1,c))
            if c-1>=0 and (not (r,c-1) in path) and board[r][c-1]==char:
                ret.add((r,c-1))
            if c+1<len(board[0]) and (not (r,c+1) in path) and board[r][c+1]==char:
                ret.add((r,c+1))
            print(ret)
            return ret
        def backtrack(path,r,c):
            if len(path)==len(word):
                return True
            print(path,r,c)
            for cand in check(path,r,c,word[len(path)]):
                print(cand)
                path.add(cand)
                r,c= cand
                if backtrack(path,r,c):
                    return True
                path.remove(cand)
            return False
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col]==word[0]:
                    path={(row,col)}
                    if backtrack(path,row,col):
                        return True
        return False
        

                        