class Node:
    def __init__(self,key=None, val=None):
        self.key=key
        self.val=val
        self.prev=None
        self.next=None
class LRUCache:

    def __init__(self, capacity: int):
        self.head=Node()
        self.tail=Node()
        self.head.next=self.tail
        self.tail.prev=self.head
        self.capacity=capacity
        self.cache={}

    def get(self, key: int) -> int:
        c=self.cache
        if not key in c:
            return -1
        node=c[key]
        form=node.prev
        lat=node.next
        form.next=lat
        lat.prev=form
        node.prev=self.head
        node.next=self.head.next
        self.head.next=node
        node.next.prev=node
        return node.val

    def put(self, key: int, value: int) -> None:
        c=self.cache
        if key in c:
            node=c[key]
            form=node.prev
            lat=node.next
            form.next=lat
            lat.prev=form
            node.val=value
        else:
            node=Node(key,value)
            c[key]=node
        
        node.prev=self.head
        node.next=self.head.next
        self.head.next=node
        node.next.prev=node
        
        if len(c) > self.capacity:
            node=self.tail.prev
            victim=node.key
            form=node.prev
            lat=node.next
            form.next=lat
            lat.prev=form
            del c[victim]

