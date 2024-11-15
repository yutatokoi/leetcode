class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        total = 0
        nums = sorted(nums)
        while nums:
            nums.pop()
            total += nums.pop()

        return total
