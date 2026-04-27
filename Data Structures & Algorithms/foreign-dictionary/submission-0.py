class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        def alnum(char):
            return ord(char)-ord('a')
        adj=defaultdict(list)
        indegree=[0 for _ in range(26)]
        exists=[False for _ in range(26)]
        for i in range(len(words)-1):
            j=0
            while words[i][j] == words[i+1][j]:
                exists[alnum(words[i][j])]=True
                j=j+1
                if j==len(words[i]):
                    break
            if j==len(words[i]):
                for k in words[i+1][j:]:
                    exists[alnum(k)]=True
                continue
            exists[alnum(words[i][j])]=exists[alnum(words[i+1][j])]=True
            adj[alnum(words[i][j])].append(alnum(words[i+1][j]))
            indegree[alnum(words[i+1][j])]+=1
        queue=deque()
        ret=""
        for i in range(26):
            if not indegree[i] and exists[i]:
                queue.append(i)
        while queue:
            c=queue.popleft()
            ret+=chr(c+ord('a'))
            for nc in adj[c]:
                indegree[nc]-=1
                if not indegree[nc]:
                    queue.append(nc)
        return ret