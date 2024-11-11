class Solution:
    def toHex(self, num: int) -> str:
        if num == 0: 
            return "0"

        hex_digits = '0123456789abcdef'
        ans = ""
        if num < 0:
            num = num + (1 << 32)
        
        while num:
            num, m = divmod(num, 16)
            ans += hex_digits[m]
        
        return ans[::-1]

        
