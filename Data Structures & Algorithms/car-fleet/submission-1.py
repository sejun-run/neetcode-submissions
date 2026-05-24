class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack=[]
        ordered=sorted(zip(position,speed))
        for position, speed in ordered:
            left=(target-position)/speed
            while stack and stack[-1] <= left:
                stack.pop()
            stack.append(left)
        return len(stack)



                
                