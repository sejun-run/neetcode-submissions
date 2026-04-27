class Node:
    def __init__(self):
        self.child={}
        self.isEnd=False
class Trie:
    def __init__(self):
        self.root=Node()
    def add(self,word):
        cur=self.root
        for w in word:
            if w not in cur.child:
                cur.child[w]=Node()
            cur=cur.child[w]
        cur.isEnd=True
    def search(self,word):
        cur=self.root
        for w in word:
            if w in cur.child:
                cur=cur.child[w]
            else:
                return False
        return True if cur.isEnd else False

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        tree=Trie()
        for word in wordDict:
            tree.add(word)
        def split(l):
            if l==len(s):
                return True
            
            for i in range(l,len(s),1):
                if tree.search(s[l:i+1]):
                    if split(i+1):
                        return True
            return False
        return split(0)
