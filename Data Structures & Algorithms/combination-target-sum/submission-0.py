from typing import List

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        
        def backtrack(index, path, target):
            if sum(path) == target:
                result.append(path[:])
                return
            if index >= len(nums) or sum(path) > target:
                return
            path.append(nums[index])
            backtrack(index, path, target)
            path.pop()
            
            backtrack(index + 1, path, target)
        backtrack(0, [], target)
        return result