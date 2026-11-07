class Solution:

    def opposite(self, one, two):
        if not one or not two:
            return False
        return (one > 0 and two < 0)

    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        
        stack.append(asteroids[0])

        for i in range(1, len(asteroids)):
            # different direction
            prev = stack[-1] if len(stack) > 0 else None
            curr = asteroids[i]
            if self.opposite(prev, curr):
                while self.opposite(prev, curr):
                    if abs(prev) == abs(curr):
                        stack.pop()
                        curr = None
                        prev = None
                    elif abs(prev) > abs(curr):
                        curr = None
                    else:
                        stack.pop()
                        prev = stack[-1] if len(stack) > 0 else None
                if curr:
                    stack.append(curr)
            else:
                stack.append(curr)
        
        return stack

                