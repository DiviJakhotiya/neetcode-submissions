class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        pref = [0]*n
        suff = [0]*n
        ans = 0
        G = prices[::-1]
        pref[0] = prices[0]
        suff[0] = G[0]
        for i in range(1 , n):
            pref[i] = min(pref[i-1] , prices[i])
            suff[i] = max(suff[i-1] , G[i])
        suff = suff[::-1]
        for i in range(n):
            ans = max(ans , suff[i] - pref[i])
        return ans


        

        