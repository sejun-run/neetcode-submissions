class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True
        prelist={}
        postlist={}
        prepath=[]
        postpath=[]
        for pre in prerequisites:
            if not prelist.get(pre[0],None):
                prelist[pre[0]]=[]
            if not postlist.get(pre[1],None):
                postlist[pre[1]]=[]
            prelist[pre[0]].append(pre[1])
            postlist[pre[1]].append(pre[0])
        def dfs(val):
            prepath.append(val)
            if val not in prelist:
                return True
            for nextval in prelist[val]:
                if nextval in prepath:
                    return False
                dfs(nextval)
            return True
        def postdfs(val):
            postpath.append(val)
            if val not in postlist:
                return True
            for nextval in postlist[val]:
                if nextval in postlist:
                    return False
                postdfs(nextval)
            return True
        return dfs(prerequisites[0][0]) and postdfs(prerequisites[0][0])