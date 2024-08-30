class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        res = []
        last_seen = lower - 1
        nums.append(upper + 1)

        for i in range(len(nums)):
            if nums[i] - last_seen > 1:
                res.append([last_seen + 1, nums[i] - 1])
            last_seen = nums[i]

        return res


