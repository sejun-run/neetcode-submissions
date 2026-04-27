class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        cntmap={}
        ret=[]
        def intoArr(s):
            ret=[0]*26
            for c in s:
                idx=ord(c)-ord('a')
                ret[idx]+=1
            return tuple(ret)

        for string in strs:
            cnt=intoArr(string)
            if cnt in cntmap:
                ret[cntmap[cnt]].append(string)
            else:
                ret.append([string])
                cntmap[cnt]=len(ret)-1
        return ret