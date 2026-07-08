class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        index, len1 = 0, 0
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j]:
                    if j - i <= 2 or dp[i + 1][j - 1]:
                        dp[i][j] = True
                        if len1 < j - i + 1:
                            index = i
                            len1 = j - i + 1
        return s[index:index + len1]