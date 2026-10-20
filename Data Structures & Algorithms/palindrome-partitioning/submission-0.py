class Solution:
    def isPalindrome(self, s):
        "".join(s)
        l = 0
        r = len(s) - 1

        res = True

        while l < r:
            if s[l] != s[r]:
                res = False
            l+=1
            r-=1
        return res
    
    def partition(self, s: str) -> List[List[str]]:
        #print(self.isPalindrome(s))

        self.res = []

        def dfs(i, sub):
            if i >= len(s):
                self.res.append(sub.copy())
                return

            for j in range(i, len(s)):
                if self.isPalindrome(s[i:j+1]):
                    sub.append(s[i:j+1])
                    dfs(j+1, sub)
                    sub.pop()

        dfs(0, [])

        return self.res