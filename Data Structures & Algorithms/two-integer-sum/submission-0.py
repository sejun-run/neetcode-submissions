class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict={}
        ret=[]*2
        for i in range[len(nums)]:
            num_dict[nums[i]]=i
        for i in range[len(nums)]:
            tar = target - nums[i]
            if num_dict[tar] :
                ret[0]=i
                ret[1]=num_dict[tar]
        return ret