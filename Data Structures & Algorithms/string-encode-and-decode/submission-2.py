class Solution:

    def encode(self, strs: List[str]) -> str:
        ret=""
        for s in strs:
            ret+=chr(len(s))
            ret+=s
        return ret
    def decode(self, s: str) -> List[str]:
        i=0
        ret=[]
        while i< len(s):
            length=ord(s[i])
            i+=1
            ret.append(s[i:i+length])
            i+=length
        return ret