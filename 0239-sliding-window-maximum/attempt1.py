class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        
        l = 0
        for r in range(k - 1, len(nums)):
            if k == 1:
                window = nums[l]
                output.append(window)
            else:
                window = nums[l : r + 1]
                output.append(max(window))

            l += 1

        return output

