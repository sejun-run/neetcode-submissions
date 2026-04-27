# 흠 그러니까 두 번 이상 등장 
# 그러면 한 번 훑고 다시 한 번 훑는 느낌 어때?
# 일단 훑으면서 어레이에 하나씩 저장하면 메모리 시간이 O(n) 이때 각각 저장할때 뭐가 있으면 바로 flag 인거지
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dup = [0]*(len(nums)*10**5)
        for n in nums:
            if dup[n] == 0:
                dup[n] = 1
            else: 
                return True
        return False