class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1 = {}
        for i in range(len(s)):
            if s[i] not in dict1:
                dict1[s[i]] = 1
            else:
                dict1[s[i]] += 1
        for i in range(len(t)):
            if t[i] not in dict1:
                return False
            dict1[t[i]] -= 1
            if dict1[t[i]] < 0:
                return False
        for i , char in dict1.items():
            if char > 0:
                return False
        return True 


        