class Solution:
    def is_pali(self, l,r, s):
        while l<r:
            if s[l] != s[r]:
                return False
            l+=1
            r-=1
        return True

    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s)-1

        mid = len(s)//2

        print(s[:mid])
        print(s[mid:][::-1])

        wrong = 0
        while l < r:
            if s[l] != s[r]:
                return self.is_pali(l+1, r, s) or self.is_pali(l, r-1, s)
            else:    
                l+=1
                r-=1
        
        return True