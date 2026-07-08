from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        counter = 0
        dirs = [(0,1),(1,0),(-1,0),(0,-1)]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    counter += 1
                    queue = deque()
                    queue.append((i, j))
                    while queue:
                        cx, cy = queue.pop()
                        if cx < 0 or cy < 0 or cx >= len(grid) or cy >= len(grid[0]) or grid[cx][cy] == "0":
                            continue
                        grid[cx][cy] = "0"
                        for dx, dy in dirs:
                            nx, ny = cx + dx, cy + dy
                            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == "1":
                                queue.append((nx, ny))
        return counter