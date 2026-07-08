class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')': '(', '}': '{', ']': '['}

        for c in s:
            if c in pairs:  # closing bracket
                if not stack or stack.pop() != pairs[c]:
                    return False
            else:  # opening bracket
                stack.append(c)

        return not stack