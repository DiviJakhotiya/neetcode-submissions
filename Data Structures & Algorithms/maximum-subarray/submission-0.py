class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max1 = nums[0]
        temp = nums[0]
        for i in range(1,len(nums)):
            temp = max(nums[i], temp + nums[i])
            max1 = max(max1, temp)
        return max1
        