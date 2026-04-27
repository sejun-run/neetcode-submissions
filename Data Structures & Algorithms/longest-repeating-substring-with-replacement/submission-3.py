class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        def topnum(map:dict):
            ret=0
            for n in map.values():
                ret=max(ret,n)
            return ret
        ret=l=0
        cmap={}
        for r in range(len(s)):
            cmap[s[r]]=cmap.get(s[r],0)+1
            while r-l+1-topnum(cmap)>k:
                cmap[s[l]]-=1
                l+=1
            ret=max(ret,r-l+1)
        return ret