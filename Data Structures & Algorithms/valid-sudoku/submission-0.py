from collections import defaultdict

def box_checker(board, r, c):
    dict1 = defaultdict(int)

    for i in range(r, r + 3):
        for j in range(c, c + 3):
            dict1[board[i][j]] += 1

    for index, value in dict1.items():
        if index != "." and value > 1:
            return False
    return True

def col_checker(board, col):
    dict1 = defaultdict(int)

    for row in range(9):
        dict1[board[row][col]] += 1

    for index, value in dict1.items():
        if index != "." and value > 1:
            return False
    return True

def row_checker(board, row):
    dict1 = defaultdict(int)

    for col in range(9):
        dict1[board[row][col]] += 1

    for index, value in dict1.items():
        if index != "." and value > 1:
            return False

    return True

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        for i in range(9):
            if not row_checker(board, i):
                return False
            if not col_checker(board, i):
                return False
        for r in range(0, 9, 3):
            for c in range(0, 9, 3):
                if not box_checker(board, r, c):
                    return False
        return True



        