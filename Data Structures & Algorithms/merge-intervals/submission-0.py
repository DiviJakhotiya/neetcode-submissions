class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        stack = []
        for i in range(len(intervals)):
            start, end = intervals[i][0], intervals[i][1]
            if not stack:
                stack.append([start, end])
                continue
            prev_start, prev_end = stack.pop()
            if start <= prev_end:
                stack.append([prev_start, max(prev_end, end)])
            else:
                stack.append([prev_start, prev_end])
                stack.append([start, end])
        return stack
            
            
            
