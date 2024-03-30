class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        l = 0
        r = 1

        if len(s) == 0:
            return 0
        else:
            curr = {s[l]}
        while r < len(s):
            if s[r] in curr:
                curr.remove(s[l])
                l += 1
                curr.add(s[r])
                r += 1
                longest = max(longest, len(curr))
            else:
                curr.add(s[r])
                r += 1
                longest = max(longest, len(curr))
        
        return longest

