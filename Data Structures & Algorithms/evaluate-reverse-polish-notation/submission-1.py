class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def operation(a,b,op):
            if op =="+":
                return(a+b)
            elif op =="-":
                return(a-b)
            elif op =="*":
                return(a*b)
            elif op =="/":
                return(a//b)
            else :
                return False
        def isop(s):
            if s =="+" or s =="-" or s =="*" or s =="/":
                return True
            else:
                return False
        stack=[]
        while len(tokens)!=0:
            t= tokens.pop()
            if isop(t):
                stack.append(t)
            elif isop(stack[-1]):
                stack.append(t)
            else :
                stack.append(operation(int(t),int(stack.pop()),stack.pop()))
            print(stack)
        while len(stack)!=1:
            stack.append(operation(int(stack.pop()),int(stack.pop()),stack.pop()))

        return int(stack.pop())
