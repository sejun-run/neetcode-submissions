class Solution:
    def climbStairs(self, n: int) -> int:
        onestep=1
        twostep=0
        for _ in range(n):
            step=onestep+twostep
            twostep=onestep
            onestep=step
        return step