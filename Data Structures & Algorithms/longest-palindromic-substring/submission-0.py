class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxcase=[0,0]
        for m in range(len(s)):
            n=0
            while 0<=m-n and m+n<len(s) and s[m-n]==s[m+n]:
                if n> maxcase[1]:
                    maxcase[0]=m
                    maxcase[1]=n
                n+=1
        oddpal= s[maxcase[0]-maxcase[1]:maxcase[0]+maxcase[1]+1]
        maxcase=[0,-1]
        for m in range(len(s)):
            n=0
            while 0<=m-n and m+1+n<len(s) and s[m-n]==s[m+1+n]:
                if n> maxcase[1]:
                    maxcase[0]=m
                    maxcase[1]=n
                n+=1
        if maxcase[1]!=-1:
            evenpal= s[maxcase[0]-maxcase[1]:maxcase[0]+maxcase[1]+2]
            if len(evenpal)>len(oddpal):
                return evenpal
        return oddpal      