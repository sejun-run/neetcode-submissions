class Solution:
    def countSubstrings(self, s: str) -> int:
        ret=0
        def expand(left:int,right:int) -> int:
            count=0
            while left>=0 and right<len(s) and s[left]==s[right]:
                count+=1
                left-=1
                right+=1
            return count
        for i in range(len(s)):
            ret+= expand(i,i)+expand(i,i+1)
        return ret