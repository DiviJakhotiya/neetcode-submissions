class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        dirs = [(-1 , 0) , (0 , -1)]
        if obstacleGrid[0][0] == 1:
            return 0
        dp = [[-1] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0 # ways to reach a place = ways to reach above it + to its left
        dp[0][0] = 1
        for i in range(n):
            for j in range(m):
                if dp[i][j] == -1:
                    dp[i][j] = 0
                    for dx , dy in dirs:
                        if  0 <= i + dx <= n -1 and 0 <= j +dy <= m-1:
                            dp[i][j] += dp[i + dx][j + dy]
        return dp[n-1][m-1]

