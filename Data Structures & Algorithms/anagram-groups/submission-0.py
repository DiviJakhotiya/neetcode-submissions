class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict1 = defaultdict(list)
        hash1 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
        for str1 in strs:
            temp = 1
            for chars in str1:
                temp = temp*(hash1[ord(chars) - ord('a')])
            dict1[temp].append(str1)
        out = []
        for index ,arr in dict1.items():
            out.append(arr)
        return out
                    