class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        one = {}
        two = {}

        return self.buildDict(s) == self.buildDict(t)

    def buildDict(self, s: str):
        build = {}
        for char in s:
            build[char] = build.get(char, 0)  +1
        return build