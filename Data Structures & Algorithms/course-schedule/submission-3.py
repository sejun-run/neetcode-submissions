class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True
        prelist={}
        safe=set()
        vertices=set()
        for pre in prerequisites:
            if not prelist.get(pre[0],None):
                prelist[pre[0]]=[]
            prelist[pre[0]].append(pre[1])
            if pre[0] not in vertices:
                vertices.add(pre[0])
        def dfs(val,prepath):
            prepath.add(val)
            if val not in prelist:
                return True
            for nextval in prelist[val]:
                if nextval in safe:
                    continue
                if nextval in prepath:
                    return False
                if not dfs(nextval,prepath.copy()):
                    return False
            safe.add(val)
            return True
        for vertice in vertices:
            print(vertice)
            if vertice not in safe:
                prepath=set()
                if not dfs(vertice,prepath):
                    return False
        return True