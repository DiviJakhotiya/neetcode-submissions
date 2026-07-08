class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max1 = 0
        stack = [] # [(0,7)]
        for i , h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index , height = stack.pop() # 0 , 7
                max1 = max(max1 , (i - index) * height)
                start = index
            stack.append((start , h))
        for i , h in stack:
            max1 = max(max1 , h*(len(heights) - i))
        return max1


        