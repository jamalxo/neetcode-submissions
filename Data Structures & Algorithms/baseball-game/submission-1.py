class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        current_op = ""

        for i in range(len(operations)):
            print(i, stack)
            curr = operations[i]
            if curr == "C":
                stack.pop()
            elif curr == "+":
                prev = stack[-1]
                prev2 = stack[-2]
                stack.append(prev+prev2)
            elif curr == "D":
                prev = stack[-1]
                stack.append(prev*2)
            else:
                stack.append(int(operations[i]))

        return sum(stack)

