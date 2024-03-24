class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while l < r:
            l_char = s[l]
            r_char = s[r]
            if not self.alpha_num(l_char) and l < r:
                l += 1
            elif not self.alpha_num(r_char) and l < r:
                r -= 1
            elif self.alpha_num(l_char) and self.alpha_num(r_char):
                if l_char.lower() != r_char.lower():
                    return False
                else:
                    l += 1
                    r -= 1
        return True

    def alpha_num(self, c):
        return (ord('a') <= ord(c) <= ord('z') or 
                ord('A') <= ord(c) <= ord('Z') or 
                ord('0') <= ord(c) <= ord('9'))

