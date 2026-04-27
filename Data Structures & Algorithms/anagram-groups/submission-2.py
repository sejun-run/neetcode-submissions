class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anags=defaultdict(list)
        for s in strs:
            counts=[0]*26
            for c in s:
                idx=ord(c)-ord("a")
                counts[idx] += 1
            anags[tuple(counts)].append(s)
        ret=[]
        for k, v in anags.items():
            ret.append(v)
        return ret