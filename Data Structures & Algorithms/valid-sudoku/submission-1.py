class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n=len(board)
        for row in board:
            group=set()
            for num in row:
                if num=='.':
                    continue
                if num in group:
                    return False
                else:
                    group.add(num)
        for col in range(n):
            group=set()
            for row in range(n):
                if board[row][col] == '.':
                    continue
                if board[row][col] in group:
                    return False
                else:
                    group.add(board[row][col])
        for i in range(3):
            for j in range(3):
                group=set()
                for t in range(3):
                    for v in range(3):
                        row=3*i+t
                        col=3*j+v
                        if board[row][col] == '.':
                            continue
                        if board[row][col] in group:
                            return False
                        else:
                            group.add(board[row][col]) 
        return True