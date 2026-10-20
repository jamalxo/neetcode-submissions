class Solution:
    def countSubstrings(self, s: str) -> int:
        #expand for each char
        counter = 0

        for i in range(len(s)):
            l = i
            r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                counter +=1
                l = l - 1
                r = r + 1
            l = i
            r = i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                counter +=1
                l = l - 1
                r = r + 1
        
        return counter