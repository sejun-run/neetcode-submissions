class Solution:

    def encode(self, strs: List[str]) -> str:
        ret=""
        for string in strs:
            ret+=str(len(string))+string
        return ret
    def decode(self, s: str) -> List[str]:
        i=0
        ret=[]
        while i < len(s):
            cnum=int(s[i])
            ret.append(s[i+1:i+1+cnum])
            i=i+1+cnum
        return ret