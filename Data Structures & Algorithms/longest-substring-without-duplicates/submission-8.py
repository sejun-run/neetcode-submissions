class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ret=l=0
        curdict={}
        for r in range(len(s)):
            if s[r] in curdict and curdict[s[r]] >= l:
                l=curdict[s[r]]+1
            curdict[s[r]]=r
            ret=max(ret,r-l+1)
        return ret