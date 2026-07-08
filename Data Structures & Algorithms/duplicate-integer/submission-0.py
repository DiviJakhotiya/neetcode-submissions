from collections import defaultdict
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict1 = defaultdict(int)
        for num in nums:
            dict1[num] += 1
            if dict1[num] > 1:
                return True
        return False
        