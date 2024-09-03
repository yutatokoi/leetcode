class Solution:
    def getLucky(self, s: str, k: int) -> int:
        while k > 0:
            res = []
            for c in s:
                if c.isdigit():
                    res.append(c)
                else:
                    res.append(str(ord(c) - ord('a') + 1))

            s = "".join(res)
            if s[0].isdigit():
                ans = 0
                for digit in s:
                    ans += int(digit)
                s = str(ans)
            
            k -= 1

        return ans

        
