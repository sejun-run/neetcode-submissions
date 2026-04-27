class Solution:
    def reverse(self, x: int) -> int:
        res=0
        sign= -1 if x<0 else 1
        x=abs(x)
        while x>0:
            pop=x%10
            x//=10
            res=res*10 +pop
        if res>((1<<31)-1):
            return 0
        return res*sign
