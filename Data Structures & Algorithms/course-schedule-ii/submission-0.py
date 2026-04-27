class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        pre=defaultdict(list)
        ret=[]
        indegree=[0 for _ in range(numCourses)]
        for prereq in prerequisites:
            pre[prereq[1]].append(prereq[0])
            indegree[prereq[0]]+=1
        queue=deque()
        for i in range(numCourses):
            if not indegree[i]:
                queue.append(i)
        print(queue)
        while queue:
            course=queue.popleft()
            ret.append(course)
            for req in pre[course]:
                indegree[req]-=1
                if indegree[req]==0:
                   queue.append(req)
        if len(ret)==numCourses:
            return ret
        else:
            return []