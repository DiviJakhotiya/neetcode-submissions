class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        hash1 = defaultdict(int)
        for chars in s:
            hash1[chars] += 1
        for chrs in t:
            hash1[chrs] -= 1
        for vals , nums in hash1.items():
            if nums < 0:
                return vals
        
        