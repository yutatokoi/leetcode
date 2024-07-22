class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        prefix = [1]
        suffix = [1]

        for i in range(1, len(nums)):
            prefix.append(nums[i - 1] * prefix[i - 1])

        nums.reverse()

        for i in range(1, len(nums)):
            suffix.append(nums[i - 1] * suffix[i - 1])

        suffix.reverse()

        for i in range(len(nums)):
            res.append(prefix[i] * suffix[i])

        return res

        
