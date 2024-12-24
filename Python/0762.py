class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        primes = {2, 3, 5, 7, 11, 13, 17, 19}

        ans = 0
        for n in range(left, right + 1):
            ans += int(bin(n).count('1') in primes)

        return ans
