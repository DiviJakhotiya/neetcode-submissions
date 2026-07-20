class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dirs = [(-1,0) , (0,-1)]
        n = len(grid)
        m = len(grid[0])
        dp = [[float('inf')] * m for _ in range(n)]
        dp[0][0] = grid[0][0]
        for i in range(n):
            for j in range(m):
                for dx , dy in dirs:
                    if 0 <= i + dx <= n - 1 and 0 <= j + dy <= m - 1:
                        dp[i][j] = min(dp[i][j] , dp[i+dx][j+dy] + grid[i][j])
        print(dp)
        return dp[n-1][m-1]
                
