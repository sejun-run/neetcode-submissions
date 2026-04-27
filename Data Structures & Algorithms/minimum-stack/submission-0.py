class MinStack:

    def __init__(self):
        self.stack=[]
        self.min=[]

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.min)!=0 and val>=self.min[-1]:
            val= self.min[-1]
        self.min.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.min.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min[-1]
