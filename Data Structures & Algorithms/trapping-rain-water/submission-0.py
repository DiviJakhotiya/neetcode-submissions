class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n == 0:
            return 0
        pref = [0] * n
        suff = [0] * n
        ans = 0
        G = height[::-1]
        pref[0] = height[0]
        suff[0] = G[0]
        for i in range(1, n):
            pref[i] = max(pref[i - 1], height[i])
            suff[i] = max(suff[i - 1], G[i])
        suff = suff[::-1]   
        for i in range(n):
            ans += max(0, min(pref[i], suff[i]) - height[i])

        return ans