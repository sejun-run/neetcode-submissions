class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for c in s:
            if c not in {']','}',')'}:
                stack.append(c)
            elif not stack:
                return False
            elif c == ']':
                if stack.pop() != '[':
                    return False
            elif c == '}':
                if stack.pop() != '{':
                    return False
            elif c == ')':
                if stack.pop() != '(':
                    return False
        return True if not stack else False