class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def hours(k):
            ret=0
            for p in piles:
                ret+=p//k
                if p%k>0:
                    ret+=1
            return ret
        all_piles=0
        max=0
        for p in piles:
            all_piles+=p
            if max<p:
                max=p
        s=(all_piles // h + 1) if all_piles % h else (all_piles // h)
        print(all_piles,s)
        e= max
        print(e)
        while s<e:
            m=(s+e)//2
            if hours(m)<=h:
                e=m
            elif hours(m)>h:
                s=m+1
        return e
                