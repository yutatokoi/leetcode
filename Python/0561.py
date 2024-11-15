# attmept1
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        total = 0
        nums = sorted(nums)
        while nums:
            nums.pop()
            total += nums.pop()

        return total

# attempt2
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        total = 0
        nums = sorted(nums)
        idx = len(nums) - 2
        while idx >= 0:
            total += nums[idx]
            idx -= 2

        return total
