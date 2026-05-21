class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        calstack=[]
        def is_op(tok:str) -> bool:
            if tok== '+' or tok == '-' or tok == '*' or tok=='/':
                return True
            return False
        for token in tokens:
            if not is_op(token):
                calstack.append(int(token))
            else:
                op=token
                operand2=calstack.pop()
                operand1=calstack.pop()
                if op=='+':
                    res= operand1+operand2
                elif op == '-':
                    res= operand1-operand2
                elif op == '*':
                    res= operand1*operand2
                else:
                    res=operand1//operand2
                    if res <0 and operand1%operand2:
                        res+=1
                calstack.append(res)
        return calstack.pop()

             