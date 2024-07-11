class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"

        ans, n = "", abs(num)

        while n:
            n, m = divmod(n, 7) #divmod returns tuple(integer division, remainder)
            ans += str(m)

        ans = ans[::-1]
        if num > 0:
            return ans
        else:
            return "-" + ans

        
