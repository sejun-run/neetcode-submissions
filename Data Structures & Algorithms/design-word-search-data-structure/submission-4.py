class Node:

    def __init__(self):
        self.children={}
        self.is_end=False

class WordDictionary:

    def __init__(self):
        self.root=Node()

    def addWord(self, word: str) -> None:
        node=self.root
        for char in word:
            if char not in node.children:
                node.children[char]=Node()
            node=node.children[char]
        node.is_end=True
                
    def search(self, word: str) -> bool:
        def dfs(idx: int, node: Node) -> bool:
            if idx==len(word):
                return node.is_end
            char=word[idx]
            if char=='.':
                for child in node.children.values():
                    if dfs(idx+1,child):
                        return True
                return False
            elif char in node.children:
                return dfs(idx+1,node.children[char])
            else:
                return False
        return dfs(0,self.root)
         
