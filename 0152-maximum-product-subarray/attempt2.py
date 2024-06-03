class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = max(nums)

        curr_max = 1
        curr_min = 1

        for n in nums:
            if n == 0:
                curr_max = 1
                curr_min = 1
                continue

            temp = curr_max
            curr_max = max(n * curr_max, n * curr_min, n)
            curr_min = min(n * temp, n * curr_min, n)

            result = max(result, curr_max)

        return result

        
