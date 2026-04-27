class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tcnt={}
        cnt=len(set(t))
        lret,rret=0,-1
        for alp in t:
            tcnt[alp]=tcnt.get(alp,0)+1
        l=0
        for r in range(len(s)):
            if tcnt.get(s[r],-1000) != -1000:
                tcnt[s[r]]=tcnt[s[r]]-1
                if tcnt[s[r]]==0:
                    cnt-=1
                while cnt ==0:
                    if rret==-1 or rret-lret>r-l:
                        rret=r
                        lret=l
                    if tcnt.get(s[l],-1000) != -1000:
                        tcnt[s[l]]=tcnt[s[l]]+1
                        if tcnt[s[l]]==1:
                            cnt+=1
                    l=l+1
        return s[lret:rret+1]