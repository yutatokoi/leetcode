# O(n^2) solution. Simple, but suboptimal
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if target == (nums[i] + nums[j]):
                    return [i, j]

# O(n) solution with just one-pass through array

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = dict()

        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in dictionary:
                return [dictionary[complement], i]
                
            dictionary[nums[i]] = i

        return []
