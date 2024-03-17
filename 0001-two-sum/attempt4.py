class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = dict()

        i = 0
        for n in nums:
            diff = target - n
            if diff in nums_dict:
                return [nums_dict[diff], i]
            else:
                nums_dict[n] = i
                i += 1

