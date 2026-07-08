class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pref = [0]*n
        suff = [1]*n
        pref[0] = nums[0]
        for i in range(1,n):
            pref[i] = pref[i-1] * nums[i]
        for i in range(n - 2, -1, -1):
            suff[i] = suff[i + 1] * nums[i + 1]
        print(suff)
        print(pref)
        ans = []
        ans.append(suff[0])
        for i in range(1,n):
            ans.append(suff[i]*pref[i-1])
        
        return ans
        
        