class Solution:
    def countBits(self, n: int) -> List[int]:
        ret=[0 for _ in range(n+1)]
        for i in range(n+1):
            if i<2:
                ret[i]=i
            k=i&1
            m=i>>1
            ret[i]=ret[k]+ret[m]
        return ret