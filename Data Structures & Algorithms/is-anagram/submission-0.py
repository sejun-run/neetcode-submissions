class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        string_dict= {}
        for c in s:
            if string_dict.get(c):
                string_dict[c] += 1
            else :
                string_dict[c] =1
        for c in t:
            if string_dict.get(c):
                string_dict[c] -= 1
            else :
                return False
        for c, num in string_dict:
            if num !=0:
                return False
        return True 