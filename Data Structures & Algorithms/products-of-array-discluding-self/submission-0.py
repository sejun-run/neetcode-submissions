class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre_array=[0]*len(nums)
        for i in range(len(nums)):
            if i ==0:
                pre_array[i]=nums[i]
                # print(pre_array) 
            else:
                pre_array[i]=pre_array[i-1]*nums[i]
                # print(pre_array) 
        print(pre_array) 
        suf_array=[0]*len(nums)
        for i in range(len(nums)-1,-1,-1):
            if i ==len(nums)-1:
                suf_array[i]=nums[i]
            else:
                suf_array[i]=suf_array[i+1]*nums[i]
        print(suf_array)
        ret=[]
        for i in range(len(nums)):
            if i ==0:
                ret.append(suf_array[i+1])
            elif i ==len(nums)-1:
                ret.append(pre_array[i-1])
            else :
                ret.append(pre_array[i-1]*suf_array[i+1])
        return ret