class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        length = len(nums)
        for _ in range(k):
            minimum_index = 0
            minimum_value = float("inf")
            i = 0
            while i < length:
                if nums[i] < minimum_value:
                    minimum_value = nums[i]
                    minimum_index = i
                i += 1
            nums[minimum_index] *= multiplier

        return nums
