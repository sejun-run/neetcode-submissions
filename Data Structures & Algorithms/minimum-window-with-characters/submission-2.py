class Solution:
    def minWindow(self, s: str, t: str) -> str:
        alcnt=[0]*(ord('z')-ord('A')+1)
        charset= set(t)
        for c in t:
            alcnt[ord(c)-ord('A')] +=1
        l=r=0
        short = ""
        cnt = len(charset)
        while l<len(s):
            if s[l] in charset:
                print(l,r)
                while cnt >0 :
                    if r == len(s):
                        return short
                    if s[r] in charset:
                        alcnt[ord(s[r])-ord('A')] -= 1
                        if alcnt[ord(s[r])-ord('A')] == 0:
                            cnt -=1
                    r=r+1
                print(s[l:r])
                if short =="" or len(short) > r-l:
                    short= s[l:r]
                alcnt[ord(s[l])-ord('A')] += 1
                if alcnt[ord(s[l])-ord('A')] == 1:
                    cnt +=1
            l=l+1
        return short
                
            
        