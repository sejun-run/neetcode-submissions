class Node:
    def __init__(self):
        self.child={}
        self.isEnd=False
        self.word=-1
class Trie:
    def __init__(self):
        self.root=Node()
    def addWord(self,word,i):
        cur= self.root
        for c in word:
            if c not in cur.child:
                cur.child[c]=Node()
            cur=cur.child[c]
        cur.isEnd=True
        cur.word=i
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        rown=len(board)
        coln=len(board[0])
        ret=[]
        def dfs(r,c,node):
            char=board[r][c]
            # print(r,c,char)
            cur_node=node.child[char]
            if cur_node.isEnd:
                ret.append(words[cur_node.word])
                cur_node.isEnd=False 
            board[r][c]='#'
            for dr,dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                nr,nc=r+dr,c+dc
                if 0<=nr<rown and 0<=nc<coln and board[nr][nc] in cur_node.child:
                    dfs(nr,nc,cur_node)
            board[r][c]=char
            if len(cur_node.child)==0:
                del node.child[char]
        wordstree=Trie()
        for i in range(len(words)):
            wordstree.addWord(words[i],i)
        root=wordstree.root
        for r in range(rown):
            for c in range(coln):
                char = board[r][c]
                if char in root.child:
                    dfs(r, c, root)
        return ret