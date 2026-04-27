class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sd={}
        for c in s:
            sd[c]=sd.get(c,0)+1
        for c in t:
            if not c in sd:
                return False
            sd[c]-=1
            if sd[c]==0:
                del sd[c]
        return not sd