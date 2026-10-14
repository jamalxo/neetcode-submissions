class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        solution = 0

        for token in tokens:
            # is operation
            if token in ["+", "-", "*", "/"]:
                two = int(stack.pop())
                one = int(stack.pop())
                stack.append(self.do_operation(token , one, two))
            else:
                stack.append(token)
        return int(stack[-1])

    def do_operation(self, char, one, two):
        if char == "+":
            return one + two
        if char == "-":
            return one - two
        if char == "*":
            return one * two
        if char == "/":
            return int(one / two)