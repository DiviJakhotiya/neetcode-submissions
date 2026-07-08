def bin_search(arr, left, right, target):
    while right >= left:
        mid = (left + right)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return right
def bin_search2(arr, left, right, target):
    while right >= left:
        mid = (left + right)//2
        if arr[mid] == target:
            return True
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return False
        
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        arr1 = [matrix[i][0] for i in range(n)]
        init = bin_search(arr1 , 0 , n-1 , target)
        return bin_search2(matrix[init], 0 , m-1, target)

        