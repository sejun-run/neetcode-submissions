class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        long=1
        while l < len(s)-1: 
            rp=k
            r=l+1
            cand=s[l]
            f=l
            while r< len(s):
                print("l-",l,s[l])
                print("r-",r,s[r])
                if s[r]!=cand:
                    rp=rp-1
                    if rp<0:
                        break
                r=r+1
            print("r finished")
            while f>0 :
                if s[f]!=cand:
                    rp=rp-1
                    if rp<0:
                        break
                f=f-1
            if long <r-f: 
                long=r-f
            l=l+1
        return long
            
        
        

