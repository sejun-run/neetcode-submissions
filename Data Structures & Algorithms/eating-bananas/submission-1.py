class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        mp=0
        if not piles:
            return 0
        for pile in piles:
            if mp<pile:
                mp=pile
        l,r=1,mp
        def check(t: int) -> int:
            time=0
            for pile in piles:
                time += pile//t
                if pile%t:
                    time+=1
            return time
        best= 1
        while l<=r:
            m=(l+r)//2
            if check(m)<=h:
                best = m
                r=m-1
            else:
                l=m+1
        return best
       