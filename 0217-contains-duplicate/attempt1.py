class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        for i in nums:
            if nums[i] in nums[i+1::]:
                return True
            else:
                return False
