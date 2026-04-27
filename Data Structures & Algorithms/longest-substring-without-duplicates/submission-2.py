class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub=dict()
        maxS=0
        for i in range(len(s)):
            print(i,s[i],sub)
            if sub.get(s[i],-1)+1:
                maxS=max(maxS,i-sub[s[i]])
            sub[s[i]]=i
        if maxS==0:
            return len(s)
        return maxS