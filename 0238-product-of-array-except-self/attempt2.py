class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []

        for i in range(len(nums)):
            if i == 0:
                prefix.append(1)
            else:
                prefix.append(prefix[i - 1] * nums[i - 1])
        
        suffix = []
        nums.reverse()

        for i in range(len(nums)):
            if i == 0:
                suffix.append(1)
            else:
                suffix.append(suffix[i - 1] * nums[i - 1])
        
        nums.reverse()
        suffix.reverse()
        result = []

        for i in range(len(nums)):
            result.append(prefix[i] * suffix[i])

        return result
        
