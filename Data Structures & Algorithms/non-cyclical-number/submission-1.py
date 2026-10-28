class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n != 1:
            
            print(seen, n)
            if n not in seen:
                seen.add(n)
                n = sum([int(c)**2 for c in str(n)])
            else:
                return False
            
        return True
        
