class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = 0#If there is a loop in a diagraph then return False, else Return True
        queue = deque()
        income_count = [0]*numCourses
        adj_list = defaultdict(list)
        for u ,v in prerequisites:
            adj_list[v].append(u)
        for i in range(len(prerequisites)):
            income_count[prerequisites[i][0]] += 1
        for i in range(numCourses):
            if income_count[i] == 0:
                queue.append(i)
        while queue:
            node = queue.popleft()
            visited = visited + 1
            for nodes in adj_list[node]:
                income_count[nodes] -= 1
                if income_count[nodes] == 0:
                    queue.append(nodes)
        return True if numCourses - visited == 0 else False

        
        