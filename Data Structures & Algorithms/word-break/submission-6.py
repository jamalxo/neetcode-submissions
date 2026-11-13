class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        cache = {}

        def dfs(curr):
            if not s.startswith(curr):
                return False

            if curr in cache:
                return cache[curr]

            if curr == s:
                return True

            res = False

            for word in wordDict:
                if dfs(curr + word):
                    res = True
            
            cache[curr] = res

            return res

        return dfs("")