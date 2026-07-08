class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        dir1 = [(0,1), (0, - 1) , (-1 , 0) , (1 , 0)]
        max1 = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    queue = deque()
                    counter = 1
                    queue.append((i , j))
                    grid[i][j] = 0
                    while queue:
                        x1 , y1 = queue.pop()
                        for dx , dy in dir1:
                            nx, ny = dx + x1 , y1 + dy
                            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                                if grid[nx][ny] == 1:
                                    queue.append((nx , ny))
                                    counter = counter + 1
                                    grid[nx][ny] = 0
                    
                    max1 = max(counter , max1)
        return max1
