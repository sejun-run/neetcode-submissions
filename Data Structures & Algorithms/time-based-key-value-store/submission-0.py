class TimeMap:

    def __init__(self):
        self.data=defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        values=self.data[key]
        values.append((timestamp,value))
        self.data[key]=values

    def get(self, key: str, timestamp: int) -> str:
        values=self.data[key]
        s=0
        e=len(values)-1
        if e<0 or values[s][0]> timestamp:
            return ""
        while s<=e:
            m=(s+e)//2
            if values[m][0]< timestamp:
                s=m+1
            elif values[m][0]> timestamp:
                e=m-1
            else:
                print(m)
                return values[m][1]
        print(e)
        return values[e][1]
