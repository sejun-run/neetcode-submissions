class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def check(path,r,c,char):
            if r-1>=0 and (not (r-1,c) in path) and board[r-1][c]==char:
                return (r-1,c)
            elif r+1<len(board) and (not (r+1,c) in path) and board[r+1][c]==char:
                return (r+1,c)
            elif c-1>=0 and (not (r,c-1) in path) and board[r][c-1]==char:
                return (r,c-1)
            elif c+1<len(board[0]) and (not (r,c+1) in path) and board[r][c+1]==char:
                return (r,c+1)
            else:
                return None
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col]==word[0]:
                    path={(row,col)}
                    for i in range(1,len(word)):
                        print(path,row,col,word[i])
                        nextcell=check(path,row,col,word[i])
                        print(nextcell)
                        if nextcell:
                            path.add(nextcell)
                            row,col = nextcell
                        else :
                            break
                    if len(path)==len(word):
                        return True
        return False

                        