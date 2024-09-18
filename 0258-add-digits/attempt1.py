class Solution:
    def addDigits(self, num: int) -> int:
        num = str(num)

        while len(num) != 1:
            digits = list(num)
            num = sum(map(int, digits))
            num = str(num)

        return int(num)

        
