class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        steps = [float('inf')] * n
        steps[n - 1] = 0  
        for i in range(n - 2, -1, -1):
            for j in range(1, nums[i] + 1):
                if i + j < n:
                    steps[i] = min(steps[i], 1 + steps[i + j])
        return steps[0]