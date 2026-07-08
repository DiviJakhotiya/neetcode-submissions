class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        index1 = 0
        index2 = 0
        s = ""
        while index1 < len(word1) and index2 < len(word2):
            s = s + word1[index1]
            index1 = index1 + 1
            s = s + word2[index2]
            index2 = index2 + 1
        if len(word1) > len(word2):
            while index1 < len(word1):
                s = s + word1[index1]
                index1 = index1 + 1
        elif len(word2) > len(word1):
            while index2 < len(word2):
                s = s + word2[index2]
                index2 = index2 + 1
        return s
        