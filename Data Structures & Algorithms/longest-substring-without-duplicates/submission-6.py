class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ret=l=0
        curdict={}
        for r in range(len(s)):
            if s[r] in curdict:
                prev=curdict[s[r]]
                for i in range(l,prev+1):
                    del curdict[s[i]]
                l=prev+1
            curdict[s[r]]=r
            ret=max(ret,len(curdict))
        return ret
                
