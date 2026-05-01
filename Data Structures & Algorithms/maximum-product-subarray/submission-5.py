class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        def noneZero(s:int,e:int) -> int:
            if s>e:
                return 0
            whole=1
            for i in range(s,e+1):
                whole*=nums[i]
            if whole<0 and s!=e:
                leftmax=rightmax=1
                while nums[s]>0:
                    leftmax*=nums[s]
                    s+=1
                leftmax*=nums[s]
                while nums[e]>0:
                    rightmax*=nums[e]
                    e-=1
                rightmax*=nums[e]
                whole /=max(leftmax,rightmax)
            return int(whole)
        ret=-float('inf')
        s=0
        for i in range(len(nums)):
            if nums[i]==0:
                ret=max(ret,noneZero(s,i-1),0)
                s=i+1
            elif i==len(nums)-1:
                ret=max(ret,noneZero(s,i))
        return ret
                