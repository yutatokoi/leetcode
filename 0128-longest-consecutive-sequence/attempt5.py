class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
            nums_set = set(nums)
            longest = 0

            for n in nums:
                if (n - 1) not in nums_set:
                    m = n
                    current = 1
                    
                    while (m + 1) in nums_set:
                        current += 1
                        m += 1

                    longest = max(longest, current)

            return longest

        
