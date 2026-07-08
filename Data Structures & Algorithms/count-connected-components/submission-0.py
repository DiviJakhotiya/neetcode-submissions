
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        def function(i):
            stack = [i]
            while stack:
                    node = stack.pop()
                    if not visited[node]:
                        visited[node] = True
                    for nodes in adj_graph[node]:
                        if not visited[nodes]:
                            visited[nodes] = True 
                            stack.append(nodes)
        adj_graph = defaultdict(list)
        visited = [False]*n
        for u ,v in edges:
            adj_graph[v].append(u)
            adj_graph[u].append(v)
        counter = 0
        for i in range(n):
            if visited[i] is False:
                counter = counter + 1
                function(i)
        return counter

        
   
            

        