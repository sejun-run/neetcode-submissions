class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        long=1
        while l < len(s)-1: 
            rp=k
            r=l+1
            while r< len(s):
                print(r,s[r])
                if s[r]!=s[l]:
                    rp=rp-1
                    if rp<0:
                        break
                r=r+1
            if long <r-l: 
                long=r-l
            l=l+1
        return long
            
        
        

