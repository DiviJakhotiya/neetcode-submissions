def function(n):
    output = 0
    while n:
        digit = n % 10
        digit = digit ** 2
        output += digit
        n = n // 10
    return output
        

class Solution:
    def isHappy(self, n: int) -> bool:
        dict1 = defaultdict(lambda: False)
        check = True
        while check:
            output = function(n)
            n = output
            if output == 1:
                return True
            if dict1[output]:
                return False
            else:
                dict1[output] = True
            


        



        