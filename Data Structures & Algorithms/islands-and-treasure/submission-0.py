class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2**31 - 1
        dir1 = [(0,1) , (1 , 0) , (-1 , 0) , (0 , -1)]
        queue = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    queue.append((i,j))
        counter = 1
        while queue:
            dx , dy = queue.popleft()
            for cx , cy in dir1:
                nx, ny = dx + cx , dy + cy
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                    queue
                    if grid[nx][ny] == INF:
                        queue.append((nx , ny))
                        grid[nx][ny] = grid[dx][dy] + 1
                counter = counter + 1 

                    

        