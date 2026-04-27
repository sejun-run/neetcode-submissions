class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seq={}
        maxn=0
        init=1
        for num in nums:
            if num in seq:
                continue
            seq[num]=seq.get(num-1,0)+seq.get(num+1,0)+1
            seq[num-seq.get(num-1,0)]=seq[num]
            seq[num+seq.get(num+1,0)]=seq[num]
            if seq[num]> maxn:
                maxn=seq[num]
                print(maxn,num)
        return maxn
            
            