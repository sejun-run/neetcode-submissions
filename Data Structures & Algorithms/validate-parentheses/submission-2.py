class Solution:
    def isValid(self, s: str) -> bool:
        valid=[]
        for c in s:
            if c == '(' or c == '{' or c == '[':
                valid.append(c)
            elif len(valid)!=0:
                if c == ')':
                    if valid.pop() != '(':
                        return False
                elif c == ']':
                    if valid.pop() != '[':
                        return False
                elif c == '}':
                    if valid.pop() != '{':
                        return False
            else:
                return False
        if len(valid)==0:
            return True
        return False
        # return True