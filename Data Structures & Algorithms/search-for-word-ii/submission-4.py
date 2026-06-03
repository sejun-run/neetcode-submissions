class Node:
    def __init__(self):
        self.kids={}
        self.word=''

class Trie:
    def __init__(self):
        self.root=Node()
    def add(self, word):
        node=self.root
        for char in word:
            if char not in node.kids:
                node.kids[char]=Node()
            node=node.kids[char]
        node.word=word
        
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie=Trie()
        for word in words:
            trie.add(word)
        node=trie.root
        n=len(board)
        m=len(board[0])
        res=[]
        visit=set()

        def dfs(r,c,node,visit) -> None:
            char=board[r][c]
            if char in node.kids:
                if node.kids[char].word:
                    res.append(node.kids[char].word)
                    node.kids[char].word=''
                for dr,dc in [(-1,0),(1,0),(0,1),(0,-1)]:
                    nr,nc=r+dr,c+dc
                    if 0<=nr<n and 0<=nc<m:
                        if (nr,nc) not in visit:
                            dfs(nr,nc,node.kids[char],visit|{(r,c)})
        for r in range(n):
            for c in range(m):
                dfs(r,c,node,visit)
        return res
        


        
