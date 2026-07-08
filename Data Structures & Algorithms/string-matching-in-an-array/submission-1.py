class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        n = len(words)
        set1 = set()
        for i in range(n):
            for j in range(n):
                if i != j:
                    if words[j] in words[i]:
                        set1.add(words[j])
        return list(set1)
        