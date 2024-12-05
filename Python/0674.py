class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        lcis = 0
        anchor = 0

        for i in range(len(nums)):
            if i and nums[i - 1] >= nums[i]:
                anchor = i
            lcis = max(lcis, i - anchor + 1)

        return lcis
