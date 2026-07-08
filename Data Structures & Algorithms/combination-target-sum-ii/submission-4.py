from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        nums = sorted(candidates)
        
        def backtrack(index, path, current_sum):
            if current_sum == target:
                result.append(list(path))
                return
            
            if index >= len(nums) or current_sum > target:
                return
            
            for i in range(index, len(nums)):
                if i > index and nums[i] == nums[i-1]:
                    continue
                if current_sum + nums[i] > target:
                    break
                
                path.append(nums[i])
                backtrack(i + 1, path, current_sum + nums[i])
                path.pop()

        backtrack(0, [], 0)
        return result