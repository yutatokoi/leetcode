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
