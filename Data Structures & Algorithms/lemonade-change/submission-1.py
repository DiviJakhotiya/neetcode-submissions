from collections import defaultdict

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        hash1 = defaultdict(int)

        for bill in bills:
            if bill == 5:
                hash1[5] += 1
            elif bill == 10:
                if hash1[5] >= 1:
                    hash1[5] -= 1
                    hash1[10] += 1
                else:
                    return False
            else:  
                if hash1[10] >= 1 and hash1[5] >= 1:
                    hash1[10] -= 1
                    hash1[5] -= 1
                elif hash1[5] >= 3:
                    hash1[5] -= 3
                else:
                    return False
        return True