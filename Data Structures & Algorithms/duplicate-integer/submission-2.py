class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash1 = defaultdict(int)
        for  i in range(len(nums)):
            hash1[nums[i]] += 1
        for vals,  freq in hash1.items():
            if freq > 1:
                return True
        return False
        