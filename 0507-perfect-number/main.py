// attempt1 Naive solution
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num % 2 == 1:
            return False

        divisors = []
        n = num // 2
        for divisor in range(1, n + 1):
            if num % divisor == 0:
                divisors.append(divisor)

        return sum(divisors) == num

// attempt2 Optimal solution
import math

class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num % 2 == 1:
            return False

        total = 0
        n = math.ceil(math.sqrt(num))
        for divisor in range(1, n):
            if num % divisor == 0:
                total += divisor
                total += num // divisor

        return total // 2 == num
