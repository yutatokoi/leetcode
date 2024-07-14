class Solution:
    def myPow(self, x: float, n: int) -> float:
        base = x
        negative = False
        
        if n == 0:
            return 1
        if n < 0:
            negative = True
            n = abs(n)
        n -= 1

        while n:
            x *= base
            n -= 1

        if negative:
            return 1 / x
        else:
            return x

        
