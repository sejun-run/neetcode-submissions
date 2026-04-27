from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tfreq=Counter(t)
        l=0
        fl=fr=None
        for r in range(len(s)):
            if s[r] in tfreq:
                tfreq[s[r]]-=1
                if tfreq[s[r]]==0:
                    valid=True
                    for val in tfreq.values():
                        valid=valid and val<=0
                    if valid:
                        print(l,r)
                        while True:
                            print(l)
                            if s[l] in tfreq:
                                print(tfreq[s[l]])
                                tfreq[s[l]]+=1
                                if tfreq[s[l]]>0:
                                    if fl is None or r-l < fr-fl:
                                        fl,fr=l,r
                                    l+=1
                                    break
                            l+=1
        return s[fl:fr+1] if fr is not None else ""
