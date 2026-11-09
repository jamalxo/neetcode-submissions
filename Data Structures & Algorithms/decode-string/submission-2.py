class Solution:
    def decodeString(self, s: str) -> str:
        stack = []


        for i in range(len(s)):
            if not s[i] == "]":
                stack.append(s[i])
            else:
                print(stack)
                to_multi = ""
                while stack[-1] != "[":
                    to_multi = stack.pop() + to_multi
                stack.pop()
                digit = ""
                while stack and stack[-1].isdigit():
                    digit = stack.pop() + digit
                adding = int(digit) * to_multi
                stack.append(adding)
            
        print(stack)

        return "".join(stack)
