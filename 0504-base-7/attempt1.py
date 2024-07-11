class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        
        res = ""
        
        if num > 0:
            while num:
                res = str(num % 7) + res
                num = num // 7
            return res
        elif num < 0:
            num = abs(num)
            while num:
                res = str(num % 7) + res
                num = num // 7
            return "-" + res        

        
