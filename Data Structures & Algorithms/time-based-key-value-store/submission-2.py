class TimeMap:

    def __init__(self):
        self.dic=defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dic[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        his=self.dic[key]
        l,r=0,len(his)-1
        value=''
        while l<=r:
            m=(l+r)//2
            if his[m][0]<=timestamp:
                value=his[m][1]
                l=m+1
            else:
                r=m-1
        return value



        
