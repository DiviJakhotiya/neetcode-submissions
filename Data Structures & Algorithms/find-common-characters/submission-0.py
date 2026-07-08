class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        hash1 = defaultdict(list)
        ans = []
        for i in range(len(words)):
            set1 = set()
            for j in range(len(words[i])):
                if words[i][j] not in set1:
                    set1.add(words[i][j])
                    hash1[words[i][j]].append(1)
                else:
                    hash1[words[i][j]][-1] += 1
        for t , vall in hash1.items():
            if len(vall) == len(words):
                for i in range(min(vall)):
                    ans.append(t)
        return ans
