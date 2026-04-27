class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        indices=[]
        ret=[0 for i in range(len(temperatures))]
        for i in range(len(temperatures)):
            while len(indices)>0 and temperatures[indices[-1]]<temperatures[i]:
                idx=indices.pop()
                ret[idx]=i-idx
            indices.append(i)
        return ret
        