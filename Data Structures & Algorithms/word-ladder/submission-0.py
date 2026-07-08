
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList.append(beginWord)
        n , m = len(wordList) , len(wordList[0])
        adj_list = [[] for _ in range(n)]
        queue = deque([len(wordList) - 1])
        counter = 0
        for i in range(n):
            for j in range(n):
                diff = 0
                for k in range(m):
                    if wordList[i][k] != wordList[j][k]:
                        diff += 1
                if diff == 1:
                    adj_list[i].append(j)
                    adj_list[j].append(i)
        start = wordList.index(beginWord)
        visited = [False] * n
        queue = deque([(start, 1)])
        visited[start] = True
        while queue:
            node, dist = queue.popleft()
            if wordList[node] == endWord:
                return dist
            for nei in adj_list[node]:
                if not visited[nei]:
                    visited[nei] = True
                    queue.append((nei, dist + 1))
        return 0
        
        



        



        