class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        dirs = [(0,1) , (1,0) , (-1, 0), (0, -1)]
        max1 = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i,j))
        while queue:
            dx , dy = queue.popleft()
            for cx , cy in dirs:
                nx, ny = cx + dx , cy + dy
                if 0 <= nx < len(grid) and 0<= ny < len(grid[0]):
                    if grid[nx][ny] == 1:
                        grid[nx][ny] = grid[dx][dy] + 1
                        queue.append((nx, ny))
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1
                max1 = max(max1 , grid[i][j])
        return max(0, max1 - 2)
        


        