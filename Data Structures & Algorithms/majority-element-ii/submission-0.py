from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hash1 = defaultdict(int)
        n = len(nums)
        ans = set()
        for num in nums:
            hash1[num] += 1
            if hash1[num] > n//3:
                ans.add(num)
        return list(ans)
