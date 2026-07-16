class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        n = len(weights)
        
        def check(weights, target , days):
            pointer1 = 0
            temp_target = 0
            counter = 1
            while pointer1 <= len(weights)-1:
                temp_target = temp_target + weights[pointer1]
                if temp_target > target:
                    counter = counter + 1
                    temp_target = weights[pointer1]
                pointer1 = pointer1 + 1
            if counter > days:
                return False
            elif counter <= days:
                return True
        left, right = max(weights), sum(weights)
        while left <= right:
            mid = (left + right)//2
            if check(weights, mid, days):
                right = mid - 1
            else:
                left = mid + 1
        return left
            
            



        