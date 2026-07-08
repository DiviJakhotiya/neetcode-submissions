class Solution:
    def solve(self, board: List[List[str]]) -> None:
        queue = deque()
        dirs = [(0,1) , (-1 ,0) , (1,0), (0,-1)]
        for i in range(len(board)): #O(n*m)
            for j in range(len(board[0])):
                if board[i][j] == "O":
                    if i == 0  or j == 0:
                        queue.append((i,j))
                        board[i][j] = "V"
                    if i == len(board) - 1 or j == len(board[0]) - 1:
                        queue.append((i,j))
                        board[i][j] = "V"
        while queue: #O(number of edge connected "O"'s i.e worst case n*m)
            x , y = queue.popleft()
            for dx , dy in dirs:
                nx , ny = dx + x , dy + y
                if 0 <= nx < len(board)  and 0 <= ny < len(board[i]):
                    if board[nx][ny] == "O":
                        board[nx][ny] = "V"
                        queue.append((nx,ny))
        for i in range(len(board)): #O(n*m)
            for j in range(len(board[0])):
                if board[i][j] == "O":
                    board[i][j] = "X"
        for i in range(len(board)): #O(n*m)
            for j in range(len(board[0])):
                if board[i][j] == "V":
                    board[i][j] = "O"
        
        


                    
                    
                
                    

        