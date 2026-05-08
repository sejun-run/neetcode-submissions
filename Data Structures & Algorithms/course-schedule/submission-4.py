class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        premap=defaultdict(list)
        visited=[0]*numCourses
        for post, pre in prerequisites:
            premap[post].append(pre)
        def dfs(post: int) -> bool:
            if post not in premap or visited[post]==1:
                return True
            visited[post]=2
            for pre in premap[post]:
                if visited[pre]==2:
                    return False
                if not dfs(pre):
                    return False
            visited[post]=1
            return True
            
        for post, pre in prerequisites:
            if not dfs(post):
                return False
        return True
            