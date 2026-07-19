class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        n = len(people)
        ans = 0
        left , right = 0 , n-1
        while left <= right:
            sum1 = people[right] + people[left]
            if sum1 > limit:
                ans += 1
                right = right - 1
            else:
                ans += 1
                right = right - 1
                left = left + 1
        return ans

        