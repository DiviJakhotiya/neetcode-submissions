class Solution:
    def sortColors(self, nums: List[int]) -> None:
        n = len(nums)
        pointer1, mid , pointer2 = 0 , 0 , n- 1
        while mid <= pointer2:
            if nums[mid] == 0:
                nums[pointer1] , nums[mid] = nums[mid] , nums[pointer1]
                pointer1 = pointer1 + 1
                mid = mid + 1
            elif nums[mid] == 2:
                nums[pointer2] , nums[mid] = nums[mid] , nums[pointer2]
                pointer2 = pointer2 - 1

            else:
                mid = mid + 1
        
                