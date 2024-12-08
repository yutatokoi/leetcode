class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        n, curr = divmod(n, 2)

        while n:
            if curr == n % 2:
                return False
            
            n, curr = divmod(n, 2)

        return True
