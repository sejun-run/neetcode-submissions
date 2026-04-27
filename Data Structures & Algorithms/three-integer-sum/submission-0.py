class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sortlist=sorted(nums)
        i,j,k=0,1,len(sortlist)-1
        ret=[]
        while j < len(sortlist)-1:
            while i<j and j<k:
                if sortlist[i]+sortlist[j]+sortlist[k]> 0:
                    k=k-1
                elif sortlist[i]+sortlist[j]+sortlist[k]< 0:
                    i=i+1
                else:
                    ret.append([sortlist[i],sortlist[j],sortlist[k]])
                    break
            j=j+1
        return ret