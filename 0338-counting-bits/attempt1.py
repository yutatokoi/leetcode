class Solution:
    def countBits(self, n: int) -> List[int]:
        def numOfOnes(m):
            res = 0
            while m:
                m = m & (m - 1)
                res += 1
            return res

        ans = []
        for i in range(n + 1):
            ans.append(numOfOnes(i))

        return ans

        
