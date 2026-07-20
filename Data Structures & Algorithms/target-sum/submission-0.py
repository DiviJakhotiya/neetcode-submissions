class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
    
        def backtrack(path, index , target):
            if index == len(nums):
                return path == target
            return(backtrack(path + nums[index] , index + 1 , target) + backtrack(path - nums[index] , index + 1 , target))
        ans = backtrack(0 , 0 , target)
        return ans