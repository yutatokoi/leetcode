class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        last = ""

        i = len(s) - 1
        while s[i] == ' ':
            i -= 1
        while i >= 0 and (s[i] != ' '):
            last = s[i] + last
            i -= 1

        return len(last)


