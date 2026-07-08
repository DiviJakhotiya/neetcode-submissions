from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        F =[0] * 2
        dict1 = defaultdict(list)
        for i in range(n):
            dict1[nums[i]].append(i)
        print(dict1.items())
        for j in range(n):
            if dict1[target - nums[j]]:
                F[0] = (min(dict1[target - nums[j]][0],j))
                F[1] =(max(dict1[target - nums[j]][0] , j))
        return F

        
        
        