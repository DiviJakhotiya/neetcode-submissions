def function(num):
    num = num + 1
    digits = []
    while num > 0:
        digits.append(num % 10)
        num = num // 10
    digits.reverse()
    return digits
    

def function2(arr):
    num = 0
    arr2 = arr[::-1]
    for i in range(len(arr)):
        num = num + arr2[i]*(10**i)
    return num
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        return function(function2(digits))


        