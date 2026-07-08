class Solution:
    def firstUniqChar(self, s: str) -> int:
        dict1 = defaultdict(int)
        index = -1
        for i in range(len(s)):
            dict1[s[i]] += 1
        for i , p in dict1.items():
            if p == 1:
                index = i
                break
        for i in range(len(s)):
            if index == s[i]:
                return i
        return -1