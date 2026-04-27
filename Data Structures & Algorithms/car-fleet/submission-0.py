class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack=[]
        positions= sorted(list(enumerate(position)),key = lambda x: x[1])
        for i in range(len(positions)):
            while len(stack)!=0 and (target-position[stack[-1]])*speed[positions[i][0]] <= (target-positions[i][1])*speed[stack[-1]]:
                stack.pop()
            stack.append(positions[i][0])
        return len(stack)