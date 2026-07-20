class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        hash1 = defaultdict(int)
        for task in tasks:
            hash1[task] += 1
        max1 = max(vals for vals in hash1.values())
        t = len(tasks)
        max_ = 0
        for vals in hash1.values():
            max_ += 1 if vals == max1 else 0
        time = (max1 - 1) * (n+1) + max_
        return max(len(tasks) , time)