class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj=defaultdict(list)
        visited=[0 for _ in range(n)]
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
        def dfs(node):
            visited[node]=1
            for cand in adj[node]:
                if not visited[cand]:
                    dfs(cand)
        count=0
        for i in range(n):
            if not visited[i]:
                dfs(i)
                count+=1
        return count