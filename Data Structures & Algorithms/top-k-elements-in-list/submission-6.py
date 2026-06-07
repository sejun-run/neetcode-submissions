class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res=[]
        nmap=Counter(nums)
        flist=[[] for _ in range(len(nums)+1)]
        for num, count in nmap.items():
            flist[count].append(num)
        for i in range(len(nums),-1,-1):
            res+=flist[i]
            k-=len(flist[i])
            if k<=0:
                return res

            