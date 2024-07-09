class Solution:
    def hammingWeight(self, n: int) -> int:
        n = bin(n)[2:]
        n = list(n)
        res = 0
        for digit in n:
            if digit == '1':
                res += 1

        return res

        
