class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub=dict()
        maxS=0
        l=0
        for i in range(len(s)):
            print(i,s[i],sub)
            if sub.get(s[i],-1)+1:
                maxS=max(maxS,i-l)
                l=sub[s[i]]+1
            sub[s[i]]=i
        maxS=max(maxS,len(s)-l)
        return maxS