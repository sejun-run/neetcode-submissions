class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        tokens= tokens[::-1]
        print(tokens)
        while len(tokens)!=1:
            a=int(tokens.pop())
            b=int(tokens.pop())
            op=tokens.pop()
            if op =="+":
                tokens.append(a+b)
            elif op =="-":
                tokens.append(a-b)
            elif op =="*":
                tokens.append(a*b)
            elif op =="/":
                tokens.append(a//b)
            else :
                return False

        return int(tokens.pop())
