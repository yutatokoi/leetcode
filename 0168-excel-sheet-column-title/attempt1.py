class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = ""

        while columnNumber > 0:
            index = (columnNumber - 1) % 26
            res = chr(index + ord('A')) + res
            columnNumber = (columnNumber - 1) // 26

        return res


        
