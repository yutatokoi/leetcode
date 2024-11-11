class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        x = 0
        while (2 ** x <= n):
            if (2 ** x == n):
                return True

            x += 1

        return False

        
