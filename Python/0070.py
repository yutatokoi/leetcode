class Solution:
    def climbStairs(self, n: int) -> int:
        fib = [1, 1]
        while len(fib) < n + 1:
            fib.append(fib[-1] + fib[-2])

        return fib[-1]

        
