def area1(heights, pointer1 , pointer2):
    return min(heights[pointer1] , heights[pointer2])*(pointer2 - pointer1)
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        pointer1, pointer2 = 0, len(heights)-1
        ans = 0
        while pointer2 > pointer1:
            area = area1(heights, pointer1 , pointer2)
            ans = max(ans , area)
            if heights[pointer1] <= heights[pointer2]:
                pointer1 = pointer1 + 1
            else:
                pointer2 = pointer2 - 1

        return ans



        