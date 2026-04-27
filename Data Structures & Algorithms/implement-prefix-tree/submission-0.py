class PrefixTree:

    def __init__(self):
        self.child={}
        self.isEnd=None

    def insert(self, word: str) -> None:
        child=self.child
        for w in word:
            if not child.get(w,0):
                child[w]=PrefixTree()
            if w ==word[-1]:
                child[w].isEnd=True
            else:
                child= child[w].child
    def search(self, word: str) -> bool:
        child=self.child
        for w in word:
            if not child.get(w,0):
                return False
            if w ==word[-1]:
                if child[w].isEnd==True:
                    return True
            else:
                child= child[w].child
        return False

    def startsWith(self, prefix: str) -> bool:
        child=self.child
        for w in prefix:
            if not child.get(w,0):
                return False
            child= child[w].child
        return True
        