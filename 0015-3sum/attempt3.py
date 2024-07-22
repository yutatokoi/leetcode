class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums = sorted(nums)
        
        for i, num_i in enumerate(nums):
            if i != 0 and num_i == nums[i - 1]:
                continue
            j, k = i + 1, len(nums) - 1

            while j < k:
                three_sum = num_i + nums[j] + nums[k]

                if three_sum == 0:
                    res.append([num_i, nums[j], nums[k]])
                    j += 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                elif three_sum > 0:
                    k -= 1
                elif three_sum < 0:
                    j += 1


        return res

        
