class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        pointer1, pointer2 = 0, len(s) - 1
        while pointer1 < pointer2:
            if not (('a' <= s[pointer1] <= 'z') or ('0' <= s[pointer1] <= '9')):
                pointer1 += 1
                continue
            if not (('a' <= s[pointer2] <= 'z') or ('0' <= s[pointer2] <= '9')):
                pointer2 -= 1
                continue
            if s[pointer1] != s[pointer2]:
                return False
            pointer1 += 1
            pointer2 -= 1
        return True