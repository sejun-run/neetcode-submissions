class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        need=Counter(s1)
        n=len(s1)
        cur=Counter(s2[:n])
        if cur==need:
            return True
        for i in range(len(s2)-n):
            cur[s2[i]]-=1
            cur[s2[i+n]]=cur.get(s2[i+n],0)+1
            if cur==need:
                return True
        return False