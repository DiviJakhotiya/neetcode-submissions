class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        ans = 0
        res = []
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if i == j:
                    ans = ans + mat[i][j]
                    res.append(mat[i][j])
                elif i == len(mat[0]) - j -1:
                    ans = ans + mat[i][j]
                    res.append(mat[i][j])
        print(res)
        return ans