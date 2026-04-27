class Solution:
    def getSum(self, a: int, b: int) -> int:
        res=0
        c=0
        for i in range(32):
            i=1<<i
            if a&i and b&i and c:
                c = 1
                res|=i
            elif (a&i and b&i) or (a&i and c) or (c and b&i):
                c = 1
            elif a&i or b&i or c:
                res|=i
                c=0
            else:
                c=0
        return res
            