class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest_sequence = 0

        for n in nums:
            if (n - 1 not in nums_set):
                i = n
                current_sequence = 1
                while i + 1 in nums_set:
                    current_sequence += 1
                    i += 1
                longest_sequence = max(longest_sequence, current_sequence)
        
        return longest_sequence

