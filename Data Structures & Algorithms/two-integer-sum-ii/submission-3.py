class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        pointer1 , pointer2 = 0 , 0
        n = len(numbers)
        check = True
        while check:
            if numbers[pointer1] + numbers[pointer2] == target:
                check = False
            elif numbers[pointer1] + numbers[pointer2] < target and pointer2 < n-1:
                pointer2 = pointer2 + 1
            else:
                pointer1 = pointer1 + 1
                pointer2 = pointer1
        return [pointer1 + 1 , pointer2 + 1]
