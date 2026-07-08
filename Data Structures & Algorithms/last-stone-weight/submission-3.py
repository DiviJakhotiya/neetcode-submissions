class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stonesneg = [-i for i in stones]
        heapq.heapify(stonesneg)

        while len(stonesneg) > 1:
            stone1 = heapq.heappop(stonesneg)
            stone2 = heapq.heappop(stonesneg)
            if stone1 != stone2:
                heapq.heappush(stonesneg, -abs(stone1 - stone2))
        if stonesneg:
            return -stonesneg[0]
        else:
            return 0

        