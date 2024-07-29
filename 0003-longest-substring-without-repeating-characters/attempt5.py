class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length_max = 0
        l = 0
        char_set = set()

        for r in range(len(s)):
            if s[r] not in char_set:
                char_set.add(s[r])
                length_max = max(length_max, r - l + 1)
            else:
                while s[r] in char_set:
                    char_set.remove(s[l])
                    l += 1
                char_set.add(s[r])

        return length_max

        
