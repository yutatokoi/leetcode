class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = 0

        def product(i, j):
            n = 1
            for k in range(i, j):
                n *= nums[k]

            return n

        for i in range(len(nums)):
            for j in range(i, len(nums)):
                result = max(result, product(i, j))

        return 0 if max(nums) == 0 else result

        
