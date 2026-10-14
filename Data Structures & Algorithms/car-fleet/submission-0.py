class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        

        # while not all at destination
        cars = []

        for i in range(len(position)):
            cars.append((position[i], speed[i]))
        
        cars.sort(reverse=True)
        
        
        times = [(target-p)/s for p,s in cars]
        

        stack = []

        for t in times:
            if not stack:
                stack.append(t)
            if stack[-1] < t:
                stack.append(t)
        return len(stack)