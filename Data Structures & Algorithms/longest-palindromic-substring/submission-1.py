class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxi=maxl=0
        tmaxi=maxt=-1
        for i in range(len(s)):
            l=0
            while i>=l and i+l<len(s) and s[i-l]==s[i+l]:
                if maxl<l:
                    maxl=l
                    maxi=i
                l+=1
            t=0
            while i>=t and i+t+1<len(s) and s[i-t] == s[i+1+t]:
                if maxt<t:
                    maxt=t
                    tmaxi=i
                t+=1
        fin_l,fin_r = maxi-maxl,maxi+maxl+1
        if maxl <= maxt:
            fin_l,fin_r = tmaxi-maxt,tmaxi+maxt+2
        return s[fin_l:fin_r]