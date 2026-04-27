class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict={}
        ret=[]
        for i in range(len(nums)):
            num_dict[nums[i]]=i
        for i in range(len(nums)):
            tar = target - nums[i]
            if tar in num_dict and num_dict[tar] !=i:
                ret.append(i)
                ret.append(num_dict[tar])
                return ret
        return ret