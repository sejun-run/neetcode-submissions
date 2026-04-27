class Solution:
    def climbStairs(self, n: int) -> int:
        cache=[1]
        ret=1
        for i in range(n-1):
            cache.append(cache[i]*(n-i)*(n-i-1)/((i+1)*n))
            ret+=int(cache[i+1])
        return ret