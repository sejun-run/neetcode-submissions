class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            seen=set()
            for r in row:
                if r!='.' and r in seen:
                    # print("here?")
                    # print(seen,r)
                    return False
                else:
                    seen.add(r)
        for i in range(9):
            seen=set()
            for j in range(9):
                if board[j][i]!='.' and board[j][i] in seen:
                    print("here??")
                    print(seen, i , j, board[j][i])
                    return False
                else:
                    seen.add(board[j][i])
        for i in range(3):
            for j in range(3):
                square=board[3*i][3*j:3*j+3]+board[3*i+1][3*j:3*j+3]+board[3*i+2][3*j:3*j+3]
                seen=set()
                for l in range(len(square)):
                    if  square[l] !='.' and square[l] in seen:
                        print("here???")
                        print(seen,l,i,j,square)
                        return False
                    else:
                        seen.add(square[l])

        return True
                
                