import math
def check(arr , num, target):
    counter = 0
    for i in range(len(arr)):
        counter = counter + math.ceil(arr[i]/num)
    if target >= counter:
        return True
    else:
        return False
        
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left , right = 1 , max(piles)
        while right >= left:
            mid = (left + right)//2
            if check(piles, mid, h):
                right = mid - 1
            else:
                left = mid + 1
        return left

        