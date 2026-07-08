from typing import List

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        row = [0] * len(grid)
        column = [0] * len(grid[0])
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    row[i] += 1
                    column[j] += 1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (row[i] > 1 or column[j] > 1):
                    ans += 1
        return ans