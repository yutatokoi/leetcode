class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        char_counts = collections.defaultdict(int)

        for c in s:
            char_counts[c] += 1

        counts = list(map(lambda x: x % 2, char_counts.values()))
        return sum(counts) == 1 or sum(counts) == 0

        
