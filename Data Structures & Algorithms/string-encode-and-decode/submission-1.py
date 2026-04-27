class Solution:

    def encode(self, strs: List[str]) -> str:
        ret=""
        for string in strs:
            ret+=chr(len(string))+string
        print(ret)
        return ret
    def decode(self, s: str) -> List[str]:
        i=0
        ret=[]
        while i < len(s):
            cnum=ord(s[i])
            print (cnum)
            ret.append(s[i+1:i+1+cnum])
            i=i+1+cnum
            print (ret)
        return ret