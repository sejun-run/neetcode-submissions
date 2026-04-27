class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.ret=[]
        def addup(i, li, sum):
            # print ("i ", i,"li ", li,"sum ", sum)
            # print("current self.ret ",self.ret)
            for j in range(i,len(nums)):
                num=nums[j]
                print(">>",li,num,sum)
                if sum+num < target:
                    li.append(num)
                    addup(j, li, sum+num)
                    li.pop()
                elif sum+num==target:
                    print(li,num)
                    li.append(num)
                    self.ret.append(li[:])
                    li.pop()
        for i in range(len(nums)):
            if nums[i] <target:
                addup(i, [nums[i]], nums[i])
            elif nums[i] == target:
                self.ret.append([nums[i]])

        return self.ret