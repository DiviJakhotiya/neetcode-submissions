class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        pref = [0]*(n+1)
        for i in range(n):
            pref[i + 1] = pref[i] + nums[i]
        def check(largest):
            subarrays = 0
            i = 0
            while i < n:
                l ,r = i + 1 , n 
                while l <= r:
                    mid = (l+r)//2
                    if pref[mid] - pref[i] <= largest:
                        l = mid + 1
                    else:
                        r = mid - 1
                subarrays += 1
                i = r
                if subarrays > k:
                    return False
            return True
        l , r = max(nums) , sum(nums)
        res = r 
        while l <= r:
            mid = (l+r)//2
            if check(mid):
                res = mid
                r = mid -1
            else:
                l = mid + 1
        return res
            

        