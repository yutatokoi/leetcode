class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        count = {}

        for i, n in enumerate(nums):
            if n in count:
                count[n].append(i)
            else:
                count[n] = [i]

        degree = max([len(i) for i in count.values()])

        return min([i[-1] - i[0] for i in count.values() if len(i) == degree]) + 1
