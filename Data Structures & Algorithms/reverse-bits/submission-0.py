class Solution:
    def reverseBits(self, n: int) -> int:
        s=1
        s|=s<<2
        s|=s<<4
        s|=s<<8
        s|=s<<16
        n=((n&s)<<1)|((n>>1)&s)
        s=(1<<2)-1
        s|=s<<4
        s|=s<<8
        s|=s<<16
        n=((n&s)<<2)|((n>>2)&s)
        s=(1<<4)-1
        s|=s<<8
        s|=s<<16
        n=((n&s)<<4)|((n>>4)&s)
        s=(1<<8)-1
        s|=s<<16
        n=((n&s)<<8)|((n>>8)&s)
        s=(1<<16)-1
        n=((n&s)<<16)|((n>>16)&s)
        return n
        

