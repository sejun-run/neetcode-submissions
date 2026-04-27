class MedianFinder:

    def __init__(self):
        self.less=[]
        self.great=[]
        self.lmax=None
        self.gmin=None

    def addNum(self, num: int) -> None:
        less=self.less
        great=self.great
        print(self.lmax,self.gmin,num)
        if self.lmax is not None and self.lmax>num:
            heapq.heappush(less,-num)
            if len(less)>len(great)+1:
                heapq.heappush(great,-heapq.heappop(less))
                self.gmin=self.lmax
                self.lmax=-heapq.heappop(less)
                heapq.heappush(less,-self.lmax)
        elif self.gmin is not None and self.gmin<num:
            heapq.heappush(great,num)
            if len(great)>len(less)+1:
                curgmin=heapq.heappop(great)
                print('cur',curgmin)
                heapq.heappush(less,-curgmin)
                self.lmax=self.gmin
                self.gmin=heapq.heappop(great)
                heapq.heappush(great,self.gmin)
        else:
            if len(less)<len(great):
                heapq.heappush(less,-num)
                self.lmax=num
            else:
                print('should be here',num)
                heapq.heappush(great,num)
                self.gmin=num
                

    def findMedian(self) -> float:
        less=self.less
        great=self.great
        print ('find median',len(less),len(great))
        if len(less)<len(great):
            return self.gmin
        if len(less)>len(great):
            return self.lmax
        return (self.gmin+self.lmax)/2
        