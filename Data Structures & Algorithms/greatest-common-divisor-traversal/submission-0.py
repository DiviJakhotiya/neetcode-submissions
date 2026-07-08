from collections import defaultdict
import math

class Solution:
    def dfs(self, adj, visited, node):
        visited[node] = True
        for nodes in adj[node]:
            if not visited[nodes]:
                self.dfs(adj, visited, nodes)
    def primecheck(self, n, dict1, n2):
        if n % 2 == 0:
            dict1[2].append(n2)
        while n % 2 == 0:
            n //= 2
        i = 3
        while i * i <= n:
            if n % i == 0:
                dict1[i].append(n2)
            while n % i == 0:
                n //= i
            i += 2
        if n > 2:
            dict1[n].append(n2)
    def canTraverseAllPairs(self, nums):
        n = len(nums)
        if n == 1:
            return True
        if 1 in nums:
            return False
        adj = [[] for _ in range(n)]
        dict1 = defaultdict(list)
        for i, num in enumerate(nums):
            self.primecheck(num, dict1, i)
        for indices in dict1.values():
            for i in range(1, len(indices)):
                u, v = indices[i - 1], indices[i]
                adj[u].append(v)
                adj[v].append(u)
        visited = [False] * n
        self.dfs(adj, visited, 0)
        return all(visited)