class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        closest = float("infinity")

        for i in range(len(nums)):
            l = i + 1
            r = len(nums) - 1

            while l < r:
                three_sum = nums[i] + nums[l] + nums[r]
                if three_sum == target:
                    closest = target
                    break
                elif three_sum < target:
                    l += 1
                else:
                    r -= 1
                
                if abs(target - three_sum) < abs(target - closest):
                    closest = three_sum

        return closest
                

        
