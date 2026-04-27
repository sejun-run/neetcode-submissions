class Solution:
    def search(self, nums: List[int], target: int) -> int:
        s,e=0,len(nums)-1
        res=e
        while s<=e:
            m=(s+e)//2
            if nums[m] < nums[s]:
                e=m
            elif nums[m] > nums[e]:
                s=m+1
            else:
                res=s
                break
        print(res)
        if nums[len(nums)-1]<target:
            s,e=0,res-1
        elif nums[len(nums)-1]>target:
            s,e=res, len(nums)-2
        else:
            return len(nums)-1
        while s<=e:
            m=(s+e)//2
            if nums[m]< target:
                s=m+1
            elif nums[m] > target:
                e=m-1
            else:
                return m
        return -1