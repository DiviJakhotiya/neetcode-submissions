class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        counter = 0
        pointer = len(s) - 1
        while pointer >= 0 and s[pointer] == " ":
            pointer -= 1
        while pointer >= 0 and s[pointer] != " ":
            pointer -= 1
            counter += 1
        return counter