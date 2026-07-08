class PrefixTree:
    def __init__(self):
        self.hash1 = defaultdict(lambda: False)
        self.hash2 = defaultdict(lambda: False)
    def insert(self, word: str) -> None:
        self.hash1[word] = True
        for i in range(1, len(word) + 1):
            self.hash2[word[:i]] = True
    def search(self, word: str) -> bool:
        return self.hash1[word]
    def startsWith(self, prefix: str) -> bool:
        return self.hash2[prefix]