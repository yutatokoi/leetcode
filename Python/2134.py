class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        k = sum(nums)
        maximum = curr = sum(nums[:k])

        n = len(nums)        
        for i in range(k, n + k):
            curr += nums[i % n]
            curr -= nums[(i - k + n) % n]
            maximum = max(maximum, curr)
        return k - maximum

        
