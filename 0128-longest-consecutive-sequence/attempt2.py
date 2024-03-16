class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest_sequence = 0

        for n in nums:
            seq_len = 1
            if (n - 1) not in nums_set:
                while (n + seq_len) in nums_set:
                    seq_len += 1
            
            longest_sequence = max(longest_sequence, seq_len)

        return longest_sequence

