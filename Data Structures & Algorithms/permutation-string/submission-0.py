class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        smap={}
        slen=0
        for s in s1:
            smap[s]=smap.get(s,0)+1
            slen+=1
        dmap={}
        for i in range(slen):
            dmap[s2[i]]=dmap.get(s2[i],0)+1
        for l in range(len(s2)-slen+1):
            if dmap==smap:
                return True
            elif l == len(s2)-slen:
                return False
            else:
                dmap[s2[l]]-=1
                if dmap[s2[l]]==0:
                    del dmap[s2[l]]
                dmap[s2[l+slen]]=dmap.get(s2[l+slen],0)+1
