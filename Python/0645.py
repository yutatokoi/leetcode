class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        count = [0] * (n + 1)

        missing, duplicate = 0, 0

        for num in nums:
            count[num] += 1

        for i in range(1, len(count)):
            if count[i] == 2:
                duplicate = i
            if count[i] == 0:
                missing = i

        return [duplicate, missing]
