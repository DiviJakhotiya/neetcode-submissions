
class Solution:
    def leastInterval(self, tasks, n):
        dict1 = defaultdict(int)
        for task in tasks:
            dict1[task] += 1
        heap = [(-freq, task) for task, freq in dict1.items()]
        heapq.heapify(heap)
        counter = 0
        while heap:
            temp = []
            cycle = 0
            for _ in range(n + 1):
                if heap:
                    freq, task = heapq.heappop(heap)
                    freq += 1  
                    if freq < 0:
                        temp.append((freq, task))
                    counter += 1
                    cycle += 1
                else:
                    break
            for item in temp:
                heapq.heappush(heap, item)
            if heap:
                counter += (n + 1 - cycle)
        return counter