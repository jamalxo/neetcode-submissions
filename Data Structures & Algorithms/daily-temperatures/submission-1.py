class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # temp + index

        results = []

        for temp in temperatures:
            results.append(0)

        
        for i, temp in enumerate(temperatures):
            # is bigger
            while stack and stack[-1][0] < temp:
                popped = stack.pop()
                index = popped[1] 
                results[index] = i - index
            stack.append([temp, i])
        return results
            