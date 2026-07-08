class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        queue = deque()
        adj_list = defaultdict(list)
        indegree = [0]*numCourses
        for u,v in prerequisites:
            indegree[u] += 1
        for u , v in prerequisites:
            adj_list[v].append(u)
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        ans = []
        while queue:
            node = queue.popleft()
            ans.append(node)
            for nodes in adj_list[node]:
                indegree[nodes] -= 1
                if indegree[nodes] == 0:
                    queue.append(nodes)
        return ans if len(ans) == numCourses else []
            
