class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_new = ""

        for c in s:
            if c.isalnum():
                s_new += c.lower()
            else:
                continue
        return s_new == s_new[::-1]

