class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = max(nums)
        for i in range(len(nums)):
            curr_sum = nums[i]
            for j in range(i, len(nums)):
                curr_sum += nums[j]
        
            max_sum = max(max_sum, curr_sum)

        return max_sum
        
