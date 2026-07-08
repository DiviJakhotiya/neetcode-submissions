class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dict1 = defaultdict(list)
        intervals = []
        ans = []
        n = len(s)
        for i in range(n):
            dict1[s[i]].append(i)
        for char , list1 in dict1.items():
            intervals.append([list1[0] , list1[-1]])
        intervals.sort()   
        merged = []
        for start, end in intervals:
            if not merged or start > merged[-1][1]:
                merged.append([start, end])
            else:
                merged[-1][1] = max(merged[-1][1], end)
        for i in range(len(merged)):
            ans.append(merged[i][1] - merged[i][0] + 1)
        return ans
        
        
                

        