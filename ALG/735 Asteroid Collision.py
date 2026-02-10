class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for ast in asteroids:
            while stack and stack[-1] > 0 and ast < 0:
                cal = ast + stack[-1]
                # if asteroid smaller than stack top, asteroid explodes, do nothing
                if cal > 0:
                    ast = 0
                # if asteroid larger than stack top, stack top explodes, keep looping 
                elif cal < 0:
                    stack.pop()
                # if equal, both explode
                else:
                    ast = 0
                    stack.pop()
                
            if ast:
                stack.append(ast)

        return stack