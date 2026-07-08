
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        queue1 = deque()
        queue2 = deque()
        grid = heights
        ans = []
        dirs = [(0,-1), (0,1), (1,0), (-1,0)]
        hash1 = defaultdict(lambda: [0, 0])
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if i == 0 or j == 0:
                    queue1.append((i,j))
                    hash1[(i,j)][0] = 1
                if i == len(grid)-1 or j == len(grid[0])-1:
                    queue2.append((i,j))
                    hash1[(i,j)][1] = 1
        
        while queue1:
            x, y = queue1.popleft()
            for dx , dy in dirs:
                cx , cy = dx +x , dy + y
                if 0 <= cx < len(grid) and 0 <= cy < len(grid[0]):
                    if grid[cx][cy] >= grid[x][y]:
                        if hash1[cx,cy][0] != 1:
                            queue1.append((cx , cy))
                            hash1[(cx,cy)][0] = 1
        while queue2:
            x, y = queue2.popleft()
            for dx , dy in dirs:
                cx , cy = dx +x , dy + y
                if 0 <= cx < len(grid) and 0 <= cy < len(grid[0]):
                    if grid[cx][cy] >= grid[x][y]:
                        if hash1[cx,cy][1] != 1:
                            queue2.append((cx , cy))
                            hash1[(cx,cy)][1] = 1
        for vals , items in hash1.items():
            if items[0] == 1 and items[1] == 1:
                ans.append([vals[0], vals[1]])
        return ans
        
        


        