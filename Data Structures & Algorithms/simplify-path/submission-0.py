class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        split = path.split("/")

        cleaned = [p for p in split if p]


        for i in range(len(cleaned)):
            if cleaned[i] == "..":
                if stack:
                    stack.pop()
            elif cleaned[i] == ".":
                continue
            else:
                stack.append(cleaned[i])

        joined = "/".join(stack)

        if not stack:
            joined = "/"
        else:
            joined = "/" + joined
        
        return joined