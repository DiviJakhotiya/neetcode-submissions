
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def bin_search1():
            left, right = 0, len(matrix) - 1
            while left <= right:
                mid = (left + right) // 2

                if matrix[mid][0] <= target <= matrix[mid][-1]:
                    return mid
                elif matrix[mid][0] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return -1
        def bin_search2(row):
            left, right = 0, len(matrix[0]) - 1
            while left <= right:
                mid = (left + right) // 2
                if matrix[row][mid] == target:
                    return True
                elif matrix[row][mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return False
        row = bin_search1()
        if row == -1:
            return False
        return bin_search2(row)