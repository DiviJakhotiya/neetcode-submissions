class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        paths = path.split("/")
        for char in paths:
            if char == "..":
                if stack:
                    stack.pop()
            elif char != "" and char != ".":
                stack.append(char)
        return "/" + "/".join(stack)