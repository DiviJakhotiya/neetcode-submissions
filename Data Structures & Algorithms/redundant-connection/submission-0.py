from collections import defaultdict, deque

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj_graph = defaultdict(list)
        def bfs(src, target):
            visited = set()
            queue = deque([src])
            while queue:
                node = queue.popleft()
                if node == target:
                    return True
                for nodes in adj_graph[node]:
                    if nodes not in visited:
                        visited.add(nodes)
                        queue.append(nodes)
            return False
        for u, v in edges:
            if u in adj_graph and v in adj_graph and bfs(u, v):
                return [u, v]
            adj_graph[u].append(v)
            adj_graph[v].append(u)