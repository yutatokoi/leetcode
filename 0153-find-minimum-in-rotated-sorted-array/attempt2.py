class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = min(nums[l], nums[r])

        while l <= r:
            m = (l + r) // 2
            if nums[m] == res:
                break
            elif nums[m] < res:
                res = nums[m]
                r = m - 1
            elif nums[m] > res:
                l = m + 1

        return res

        
