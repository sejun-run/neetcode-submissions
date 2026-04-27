class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        rown=len(board)
        coln=len(board[0])
        ret=[]
        def check(path,r,c,char):
            print('checking',r,c,'for',char)
            ret=set()
            if r-1>=0 and (r-1,c) not in path and board[r-1][c]==char:
                ret.add((r-1,c))
            if r+1<rown and (r+1,c) not in path and board[r+1][c]==char:
                ret.add((r+1,c))
            if c-1>=0 and (r,c-1) not in path and board[r][c-1]==char:
                ret.add((r,c-1))
            if c+1<coln and (r,c+1) not in path and board[r][c+1]==char:
                ret.add((r,c+1))
            print(ret)
            return ret
        def dfs(path,r,c,wnum,cnum):
            print(path,r,c,cnum)
            if cnum==len(words[wnum]):
                return True
            for cand in check(path,r,c,words[wnum][cnum]):
                r,c = cand
                path.add(cand)
                if dfs(path,r,c,wnum,cnum+1):
                    return True
                path.remove(cand)
            return False
        def findfirstchar(char):
            ret=[]
            for r in range(rown):
                for c in range(coln):
                    if board[r][c]==char:
                        ret.append((r,c))
            return ret
        for i in range(len(words)):
            print(words[i])
            for r,c in findfirstchar(words[i][0]):
                print(r,c)
                path={(r,c)}
                if dfs(path,r,c,i,1):
                    ret.append(words[i])
        return ret