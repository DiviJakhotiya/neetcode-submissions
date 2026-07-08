
def sum1(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        min_dist = [float('inf')] * n
        visited = [False] * n
        min_dist[0] = 0
        ans = 0
        for _ in range(n):
            node = -1
            for i in range(n):
                if not visited[i] and (node == -1 or min_dist[i] < min_dist[node]):
                    node = i
            visited[node] = True
            ans += min_dist[node]
            for j in range(n):
                if not visited[j]:
                    dist = sum1(points[node], points[j])
                    if dist < min_dist[j]:
                        min_dist[j] = dist
        return ans