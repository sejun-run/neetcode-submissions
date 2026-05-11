class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj=defaultdict(list)
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        visited=set()
        def dfs(i: int, prev: int) -> None:
            if i in visited:
                return False
            visited.add(i)
            for node in adj[i]:
                if node == prev:
                    continue
                if not dfs(node, i):
                    return False
            return True
        return len(visited)==n if dfs(0,-1) else False