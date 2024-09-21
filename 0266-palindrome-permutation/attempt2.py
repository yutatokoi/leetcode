class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        char_counts = [0] * 26

        for c in s:
            char_counts[ord(c) - ord('a')] += 1

        counts = list(map(lambda x: x % 2, char_counts))
        return sum(counts) == 1 or sum(counts) == 0

        
