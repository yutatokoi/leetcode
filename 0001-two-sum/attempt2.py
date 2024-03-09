class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        array_map = {}

        for i, n in enumerate(nums):
            diff = target - n

            if diff in array_map:
                return [array_map[diff], i]
            array_map[n] = i
        return

