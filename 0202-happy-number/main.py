class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()

        while n not in visited:
            if n == 1:
                return True

            visited.add(n)
            n = self.sumOfSquares(n)

        return False

    def sumOfSquares(self, n: int) -> int:
        output = 0

        while n:
            digit = n % 10
            digit = digit ** 2
            output += digit
            n = n // 10
        return output

        
