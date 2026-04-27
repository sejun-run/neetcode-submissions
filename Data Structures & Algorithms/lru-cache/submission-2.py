class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.cache={}
        self.head=None
        self.tail=None

    def get(self, key: int) -> int:
        print('getting ',key,'head',self.head)
        c=self.cache
        if not key in c:
            return -1
        val=c[key][0]
        prev=c[key][1]
        next=c[key][2]
        if prev is None and next is None:
            return val
        if prev in c:
            c.get(prev)[2]=next
        else:
            self.head=next
        if next in c:
            c.get(next)[1]=prev
        else:
            self.tail=prev
        c[key][1]=None
        c[key][2]=self.head
        c[self.head][1]=key
        self.head=key
        print('get value from',key)
        return val
    def put(self, key: int, value: int) -> None:
        print('put key ',key,"with ",value)
        c=self.cache
        if not self.head:
            c[key]=[value,None,None]
            self.head=self.tail=key
        else:
            if key in c:
                val=c[key][0]
                prev=c[key][1]
                next=c[key][2]
                if prev in c:
                    c.get(prev)[2]=next
                else:
                    self.head=next
                if next in c:
                    c.get(next)[1]=prev
                else:
                    self.tail=prev
                del c[key]
            c[key]=[value,None,self.head]
            c[self.head][1]=key
            self.head=key
        if len(c) > self.capacity:
            ntail=c[self.tail][1]
            del c[self.tail]
            self.tail=ntail
            if ntail is None:
                self.head=None
            else:
                c[ntail][2]=None

        
