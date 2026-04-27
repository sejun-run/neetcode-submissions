class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tcnt={}
        cnt=len(set(t))
        lret,rret=0,-1
        for alp in t:
            tcnt[alp]=tcnt.get(alp,0)+1
        l=0
        for r in range(len(s)):
            if tcnt.get(s[r],-1) != -1:
                print("r",s[r])
                tcnt[s[r]]=tcnt[s[r]]-1
                if tcnt[s[r]]==0:
                    cnt-=1
                while cnt ==0:
                    print("l",s[l])
                    if rret==-1 or rret-lret>r-(l-1):
                        rret=r
                        lret=l-1
                    if tcnt.get(s[l],-1) != -1:
                        tcnt[s[l]]=tcnt[s[l]]+1
                        if tcnt[s[l]]==1:
                            cnt+=1
                    l=l+1
                print("window",l-1,r)
        return s[lret:rret+1]