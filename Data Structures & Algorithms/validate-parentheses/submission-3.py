class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if len(s)%2 == 1:
            return False
        for i in range(len(s)):
            if s[i] == "(" or s[i] == "{" or s[i] == "[":
                stack.append(s[i])
            else:
                if stack:
                    char = stack.pop()
                    print(char)
                    #print
                    if char == "[" and s[i] != "]":
                        return False
                    elif char == "{" and s[i] != "}":
                        return False
                    elif char == "(" and s[i] != ")":
                        return False
                else:
                    return False
        return len(stack) == 0

        