class WordNode:
    def __init__(self):
        self.child={}

class WordDictionary:

    def __init__(self):
        self.root= WordNode()

    def addWord(self, word: str) -> None:
        cur=self.root
        for w in word:
            if not cur.child.get(w,0):
                cur.child[w]=WordNode()
            cur= cur.child[w]

    def search(self, word: str) -> bool:
        def dfs(node,word):
            if len(word)==0:
                return True
            if word[0]=='.':
                for _,child in node.child.items():
                    if dfs(child,word[1:]):
                        return True
                return False
            elif not node.child.get(word[0],0):
                return False
            else :
                return dfs(node.child[word[0]],word[1:])
        return dfs(self.root,word)