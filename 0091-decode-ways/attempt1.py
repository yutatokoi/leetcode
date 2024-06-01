class Solution:
    def numDecodings(self, s: str) -> int:
        digits = [str(i) for i in range(1, 27)]
        alphabets = [chr(i) for i in range(65, 91)]

        mapping = dict(zip(digits, alphabets))

        count = 0

        for i in range(len(s)):
            

        
