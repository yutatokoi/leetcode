# attempt1: naive recursive solution
class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1

        return self.fib(n - 1) + self.fib(n - 2)

# attempt2: DP (?) solution
class Solution:
    def fib(self, n: int) -> int:
        numbers = [0] * 31
        numbers[1] = 1
        for i in range(2, n + 1):
            numbers[i] = numbers[i-1] + numbers[i - 2]

        return numbers[n]
