class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxStreak = 0
        i = 0
        n = len(nums)
        
        while i < n:
            currStreak = 0
            while i < n and nums[i] == 1:
                currStreak += 1
                maxStreak = max(maxStreak, currStreak)
                i += 1
            i += 1

        return maxStreak
