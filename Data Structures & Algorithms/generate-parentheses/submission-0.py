class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.res = []


        def dfs(openN, closeN, stack):
            
            if openN == closeN == n:
                self.res.append("".join(stack))
                return
            
            # every open needs a close
            if openN < n:
                stack.append("(")
                dfs(openN+1, closeN, stack)
                stack.pop()

            if closeN < openN:
                stack.append(")")
                dfs(openN, closeN+1, stack)
                stack.pop()
        

        dfs(0, 0, [])

        return self.res