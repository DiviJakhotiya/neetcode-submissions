from typing import List
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_list = [[] for _ in range(n)]
        for u, v, weight in times:
            adj_list[u-1].append((v-1, weight))
        dist = [float('inf')] * n
        dist[k-1] = 0
        minHeap = [(0, k-1)]
        while minHeap:
            weight, node = heapq.heappop(minHeap)
            if weight > dist[node]:
                continue
            for nodes, weights in adj_list[node]:
                if weight + weights < dist[nodes]:
                    dist[nodes] = weight + weights
                    heapq.heappush(minHeap, (dist[nodes], nodes))
        ans = max(dist)
        return ans if ans != float('inf') else -1
