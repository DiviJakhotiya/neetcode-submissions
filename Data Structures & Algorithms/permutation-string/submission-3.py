class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hash1 = 1
        map1 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
        for i in range(len(s1)):
            hash1 = hash1*map1[(ord(s1[i]) - ord("a"))]
        n = len(s1)
        tempHash = 1
        if len(s1) > len(s2):
            return False
        for i in range(n):
            tempHash *= map1[ord(s2[i]) - ord('a')]

        if tempHash == hash1:
            return True
        for right in range(n, len(s2)):
            left = right - n
            tempHash //= map1[ord(s2[left]) - ord('a')]   
            tempHash *= map1[ord(s2[right]) - ord('a')]   
            if tempHash == hash1:
                return True
        return False
        



        

        

        