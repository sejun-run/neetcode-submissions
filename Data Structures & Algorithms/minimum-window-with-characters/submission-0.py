class Solution:
    def minWindow(self, s: str, t: str) -> str:
        alcnt=[0]*(ord('z')-ord('A')+1)
        for c in t:
            alcnt[ord(c)-ord('A')] +=1
        l=0
        short = ""
        while l<len(s):
            print("next l",l,alcnt[ord(s[l])-ord('A')])
            if alcnt[ord(s[l])-ord('A')] !=0:
                print("l",l,s[l])
                scnt = alcnt.copy()
                cnt = len(t)
                r= l
                while r < len(s):
                    if scnt[ord(s[r])-ord('A')] >0:
                        scnt[ord(s[r])-ord('A')] -= 1
                        cnt -=1
                        if cnt ==0:
                            if short =="" or len(short) > r-l+1:
                                short= s[l:r+1]
                            break 
                    r=r+1
            l=l+1
        return short
                
            
        