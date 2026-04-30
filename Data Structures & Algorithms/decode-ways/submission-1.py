class Solution:
    def numDecodings(self, s: str) -> int:
        decode1=decode2=1
        for i in range(len(s)):
            decode=0
            if int(s[i])!=0:
                decode+=decode1
            if i>0 and 10<=int(s[i-1:i+1])<=26:
                decode+=decode2
            decode1,decode2=decode,decode1
        return decode1