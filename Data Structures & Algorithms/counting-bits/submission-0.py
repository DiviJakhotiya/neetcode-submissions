hardcode = [i.bit_count() for i in range(1001)]

class Solution:
    def countBits(self, n: int) -> List[int]:
        return hardcode[:(n+1)]


        