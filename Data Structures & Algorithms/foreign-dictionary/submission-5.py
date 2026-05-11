class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        if len(words)==1:
            return words[0]
        order=defaultdict(list)
        degree={}
        for i in range(1,len(words)):
            prev=words[i-1]
            cur=words[i]
            for p in prev:
                if p not in degree:
                    degree[p]=0
            for c in cur:
                if c not in degree:
                    degree[c]=0
            flag=False
            for p,c in zip(prev,cur):
                if p==c:
                    continue
                else:
                    order[p].append(c)
                    degree[c]=degree.get(c,0)+1
                    flag=True
                    break
            if not flag and len(prev)>len(cur):
                return ""
        queue=deque([])
        for al, indegree in degree.items():
            if indegree==0:
                queue.append(al)
        tot=0
        ret=""
        while queue:
            tot+=1
            al=queue.popleft()
            ret+=al
            for left in order[al]:
                degree[left]-=1
                if degree[left]==0:
                    queue.append(left)
        return ret if tot==len(degree) else ""    
        
                