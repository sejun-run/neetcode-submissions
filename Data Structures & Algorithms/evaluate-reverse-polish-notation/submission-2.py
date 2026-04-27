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
            stack.append(tokens.pop())
            if len(stack)>=3 and isop(stack[-1]) and isop(stack[-2]) and not isop(stack[-3]):
                stack.append(operation(int(stack.pop()),int(stack.pop()),stack.pop()))
            print(stack)
        while len(stack)!=1:
            stack.append(operation(int(stack.pop()),int(stack.pop()),stack.pop()))
        return int(stack.pop())
