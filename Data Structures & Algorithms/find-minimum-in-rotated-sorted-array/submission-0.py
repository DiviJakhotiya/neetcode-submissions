class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = 0 , n-1
        while right > left:
            mid = (left + right)//2
            if nums[left] < nums[right]:
                return nums[left]
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right =  mid
        return nums[left]      
                




        