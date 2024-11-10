class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m = len(needle)
        n = len(haystack)

        for l in range(n - m + 1):
            for r in range(m):
                if needle[r] != haystack[l + r]:
                    break
                if r == m - 1:
                    return l

        return -1

        
