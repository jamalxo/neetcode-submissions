class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s)-1

        while r > l:
            print(l,r)

            
            if not s[l].isalnum():
                l += 1
                continue

            if not s[r].isalnum():
                r -= 1
                continue

            print(s[l],s[r])

            if s[r].upper() != s[l].upper():
                return False
            l += 1
            
            r -= 1
        return True