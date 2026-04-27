class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanum=[]
        for c in s:
            if ord("a")<=ord(c)<=ord("z") or ord("A")<=ord(c)<=ord("Z") or ord("0")<=ord(c)<=ord("9"):
                alphanum.append(c.lower())
        length=len(alphanum)
        print(alphanum)
        for i in range(length//2):
            if alphanum[i] != alphanum[length-i-1]:
                print(alphanum[i],alphanum[length-i-1])
                return False
        return True