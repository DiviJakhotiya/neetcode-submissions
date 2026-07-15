class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        n = len(nums)
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = 0
        for i in range(n):
            if 1 <= abs(nums[i]) <= n:
                if nums[abs(nums[i]) - 1] > 0:
                    nums[abs(nums[i]) - 1] *= -1
                elif nums[abs(nums[i]) - 1] == 0:
                    nums[abs(nums[i]) - 1] = -1 * (n + 1)
        for i in range(n):
            if nums[i] >= 0:
                return i + 1
        return n + 1