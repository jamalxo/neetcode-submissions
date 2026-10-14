class Solution:
    def isValid(self, s: str) -> bool:
        
        brackets = {
            "(" : ")",
            "{" : "}",
            "[" : "]"
        }

        opens = {"(", "{", "["}

        stack = []
        previous = ""

        for c in s:
            print(stack)
            if c in opens:
                stack.append(c)
                previous = c
            elif previous and brackets[previous] == c:
                stack.pop()
                previous = stack[-1] if stack else ""
                
            else:
                return False
        return len(stack) == 0
            
