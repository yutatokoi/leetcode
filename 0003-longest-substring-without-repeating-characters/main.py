class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        l = 0
        letters = set()
        
        for r in range(len(s)):
            if s[r] in letters:
                while s[r] in letters:
                    letters.remove(s[l])
                    l += 1
            else:
                longest = max(longest, r - l + 1)
            letters.add(s[r])

        return longest


