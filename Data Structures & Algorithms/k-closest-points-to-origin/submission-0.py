def sqrt1(arr1):
    x1 , y1 = arr1[0] , arr1[1]
    x2 , y2 = 0, 0
    result = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)# O(1)
    return result
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        res = []
        heapq.heapify(heap)
        for i in range(k):
            heapq.heappush(heap, (-sqrt1(points[i]), points[i]))
        for i in range(k, len(points)):
            heapq.heappush(heap, (-sqrt1(points[i]), points[i]))
            heapq.heappop(heap)
        for i in range(len(heap)):
            res.append(heap[i][1])
        return res





        