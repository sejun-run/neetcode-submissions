class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sortlist=sorted(nums)
        j=1
        ret=set()
        while j < len(sortlist)-1:
            i,k=0,len(sortlist)-1
            while i<j and j<k:
                if sortlist[i]+sortlist[j]+sortlist[k]> 0:
                    k=k-1
                elif sortlist[i]+sortlist[j]+sortlist[k]< 0:
                    i=i+1
                else:
                    ret.add(tuple([sortlist[i],sortlist[j],sortlist[k]]))
                    k=k-1
                    i=i+1
            j=j+1
        rlist=[]
        for s in ret:
            rlist.append(list(s))
        return rlist