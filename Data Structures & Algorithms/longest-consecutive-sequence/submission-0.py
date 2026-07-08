class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dict1 = defaultdict(int)
        for num in nums:
            dict1[num] = 1
        ans = 0
        for num in nums:
            while dict1[num]:
                num -= 1
            num += 1 
            counter = 0
            while dict1[num]:
                counter += 1
                num += 1
            ans = max(ans, counter)
        return ans