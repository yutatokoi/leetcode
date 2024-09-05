class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res = 0
        for c in columnTitle:
            current_val = ord(c) - ord('A') + 1
            res = res * 26 + current_val

        return res

        
