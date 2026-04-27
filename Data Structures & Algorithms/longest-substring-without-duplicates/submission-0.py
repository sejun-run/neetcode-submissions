class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub=dict()
        maxS=0
        for i in range(len(s)):
            if sub.get(s[i]):
                maxS=max(maxS,i-sub[s[i]])
            sub[s[i]]=i
        return maxS