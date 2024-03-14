class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_sequence = 0
        nums_set = set(nums)

        for n in nums:
            seq = []
            if n-1 not in nums_set:
                seq.append(n)
                while seq[len(seq) - 1] + 1 in nums_set:
                    seq.append(seq[len(seq) - 1] + 1)

            seq_len = len(seq)
                
            if seq_len >  longest_sequence:
                longest_sequence = seq_len

        return longest_sequence

