class Solution:
    def jump(self, nums: List[int]) -> int:
        min_jumps = 0
        nums[len(nums) - 1] = 0

        for i in range(len(nums) - 1, -1, -1):
            for step in range(nums[i]):
                if i + step < len(nums):
                    nums[i] = min(nums[i], nums[i + step])

        return nums[0]

        
