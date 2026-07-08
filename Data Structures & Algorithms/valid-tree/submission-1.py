class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj_list = defaultdict(list)
        degrees = [0]*n
        visited = set()
        queue = deque()
        for u ,v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        stack = [0]
        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
            for nodes in adj_list[node]:
                if nodes not in visited:
                    visited.add(nodes)
                    stack.append(nodes)
        if len(visited) == n and len(edges) == n-1:
            return True
        else:
            print(len(visited))
            return False
            

        
        
        