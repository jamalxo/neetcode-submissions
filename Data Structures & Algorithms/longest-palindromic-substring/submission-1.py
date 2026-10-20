class Solution:
    def isPalindrome(s):
        l = 0
        r = len(s)-1
        res = True
        while l < r:
            if s[l] != [r]:
                res = False
                break
            l+=1
            r-=1
        return res
    
    def longestPalindrome(self, s: str) -> str:
        #expand for each char

        longest = ""

        for i in range(len(s)):
            l = i
            r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                sub = s[l:r+1]
                
                longest = sub if len(sub) > len(longest) else longest
                l = l - 1
                r = r + 1
            l = i
            r = i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                sub = s[l:r+1]
                
                longest = sub if len(sub) > len(longest) else longest
                l = l - 1
                r = r + 1
        
        return longest