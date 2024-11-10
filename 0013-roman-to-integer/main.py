class Solution:
    def romanToInt(self, s: str) -> int:
        digits = {"I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000}
        res = 0

        for i in range(len(s)):
            res += digits[s[i]]
            if i > 0:
                if s[i] == "V" and s[i - 1] == "I":
                    res -= 2
                elif s[i] == "X" and s[i - 1] == "I":
                    res -= 2
                elif s[i] == "L" and s[i - 1] == "X":
                    res -= 20
                elif s[i] == "C" and s[i - 1] == "X":
                    res -= 20
                elif s[i] == "D" and s[i - 1] == "C":
                    res -= 200
                elif s[i] == "M" and s[i - 1] == "C":
                    res -= 200

        return res

        
