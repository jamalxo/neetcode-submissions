class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        cache = [None] * len(s)

        def dfs(i):
            if i == len(s):
                return True
            if cache[i] is not None:
                return cache[i]

            sub = s[i:]            

            res = None

            for word in wordDict:
                if word == sub[0:len(word)]:
                    res = dfs(i+len(word))
                    if res:
                        cache[i] = True
                        return True

            cache[i] = False
            return cache[i]

        test = dfs(0)

        #print(cache)

        return test if test else False