class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nmap={}
        for num in nums:
            nmap[num]=nmap.get(num,0)+1
        most=[[] for _ in range(len(nums)+1)]
        for num, freq in nmap.items():
            most[freq].append(num)
        cnt=0
        ret=[]
        for i in range(len(nums),-1,-1):
            items=most[i]
            for item in items:
                ret.append(item)
                cnt+=1
            if cnt>=k:
                break
        return ret