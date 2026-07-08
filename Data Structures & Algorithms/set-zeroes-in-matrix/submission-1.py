from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n, m = len(matrix), len(matrix[0])
        
        first_row_zero = False
        first_col_zero = False
        
        # Check first row
        for j in range(m):
            if matrix[0][j] == 0:
                first_row_zero = True
        
        # Check first column
        for i in range(n):
            if matrix[i][0] == 0:
                first_col_zero = True
        
        # Use first row/col as markers
        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        if first_row_zero:
            for j in range(m):
                matrix[0][j] = 0
        if first_col_zero:
            for i in range(n):
                matrix[i][0] = 0