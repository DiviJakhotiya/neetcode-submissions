class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        intervals = []
        max1 = 0
        for i in range(len(trips)):
            max1 = max(trips[i][2] , max1)
            intervals.append([trips[i][1] , trips[i][2] , trips[i][0]])
        intervals.sort()
        new_arr = [0] * (max1 + 1)
        for i in range(len(intervals)):
            new_arr[intervals[i][0]] += intervals[i][2]
            new_arr[intervals[i][1]] -= intervals[i][2]
        pref = [0] * max1
        pref[0] = new_arr[0]
        for i in range(1 , max1):
            pref[i] = pref[i-1] + new_arr[i]
        if max(pref) > capacity:
            return False
        return True
        