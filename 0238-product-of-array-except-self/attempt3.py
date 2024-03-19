class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        prefix = []
        suffix = []

        for i in range(len(nums)):
            if i == 0:
                prefix.append(1)
            else:
                prefix.append(nums[i - 1] * prefix[i - 1])
        nums.reverse()
        for i in range(len(nums)):
            if i == 0:
                suffix.append(1)
            else:
                suffix.append(nums[i - 1] * suffix[i - 1])
        suffix.reverse()
        for i in range(len(nums)):
            result.append(prefix[i] * suffix[i])
        return result

