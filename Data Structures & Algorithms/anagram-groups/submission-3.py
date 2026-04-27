from collections import Counter, defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        cntmap={}
        ret=[]
        for string in strs:
            cnt=frozenset(Counter(string))
            if cnt in cntmap:
                ret[cntmap[cnt]].append(string)
            else:
                ret.append([string])
                cntmap[cnt]=len(ret)-1
        return ret