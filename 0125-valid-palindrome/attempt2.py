class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not self.alphaNum(s[l]):
                l += 1
            while r > l and not self.alphaNum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True

    def alphaNum(self, c):
        upperString = ord('A') <= ord(c) <= ord('Z')
        lowerString = ord('a') <= ord(c) <= ord('z')
        numeric = ord('0') <= ord(c) <= ord('9')
        return upperString or lowerString or numeric

