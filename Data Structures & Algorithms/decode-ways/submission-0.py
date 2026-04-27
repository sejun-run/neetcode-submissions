class Solution:
    def numDecodings(self, s: str) -> int:
        cache=[1]*(len(s)+1)
        i=len(s)-1
        while i>=0:
            if s[i]=='0':
                if i>0 and (s[i-1]=='1' or s[i-1]=='2'):
                    cache[i-1]=cache[i+1]
                    cache[i]=0
                    i-=2
                else:
                    return 0
            elif i+1<len(s) and (s[i]=='1' or (s[i]=='2' and int(s[i+1])<=6)):
                cache[i]=cache[i+1] + cache[i+2]
                i-=1
            else:
                cache[i]=cache[i+1]
                i-=1
        return cache[0]