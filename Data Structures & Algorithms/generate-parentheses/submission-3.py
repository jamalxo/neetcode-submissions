class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        mapped = {"(": 0, ")": 0}

        def dfs(s):
            if mapped["("] > n or mapped[")"] > n:
                return
            if len(s) == n*2:
                if mapped["("] == mapped[")"]:
                    res.append(s)
                return

            for k,v in mapped.items():
                if k == ")" and mapped["("] > mapped[")"]:
                    mapped[k] += 1
                    dfs(s+k)
                    mapped[k] -= 1
                if k == "(":
                    mapped[k] += 1
                    dfs(s+k)
                    mapped[k] -= 1

        dfs("")
        return res