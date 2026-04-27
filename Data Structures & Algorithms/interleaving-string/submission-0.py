class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        l1=len(s1)
        l2=len(s2)
        l3=len(s3)
        if l1+l2!=l3:
            return False
        cache={}
        def dfs(l,r):
            if l==l1:
                cache[(l,r)]= s2[r:]==s3[l+r:]
                return cache[(l,r)] 
            if r==l2:
                cache[(l,r)]= s1[l:]==s3[l+r:]
                return cache[(l,r)]
            if (l,r) in cache:
                return cache[(l,r)]
            cur=s3[l+r]
            if cur==s1[l] and dfs(l+1,r):
                cache[(l,r)]=True
                return cache[(l,r)]
            if cur==s2[r] and dfs(l,r+1):
                cache[(l,r)]=True
                return cache[(l,r)]
            cache[(l,r)]=False
            return cache[(l,r)]
        return dfs(0,0)
