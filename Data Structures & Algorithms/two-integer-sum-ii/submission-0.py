class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,r= 0,len(numbers)-1
        while l<r:
            rn=numbers[r]
            ln=numbers[l]
            if rn+ln<target:
                l=l+1
                print (l,r)
            elif rn+ln>target:
                r=r-1
                print (l,r)
            else:
                return [l+1,r+1]
        print(l,r)