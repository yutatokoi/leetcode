class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        for i in range(len(nums)):
            if i == 0:
                prefix.append(1)
            else:
                prefix.append(prefix[i - 1] * nums[i - 1])
        
        nums.reverse()
        suffix = []
        for j in range(len(nums)):
            if j == 0:
                suffix.append(1)
            else:
                suffix.append(suffix[j - 1] * nums[j - 1])
        suffix.reverse()

        result = []
        for k in range(len(nums)):
            result.append(prefix[k] * suffix[k])

        return result

