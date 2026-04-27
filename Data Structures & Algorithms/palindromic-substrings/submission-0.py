class Solution:
    def countSubstrings(self, s: str) -> int:
        count=0
        def expand(l,r,count):
            while l>=0 and r < len(s):
                if s[l]==s[r]:
                    count+=1
                    l=l-1
                    r=r+1
                else:
                    break
            return count
        for i in range(len(s)):
            count=expand(i,i,count)
            count=expand(i,i+1,count)
        return count