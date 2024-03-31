class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        
        l = 0
        
        def maxSlidingWindowHelper(prevWindowMax, r):
            if r > prevWindowMax:
                output.append(r)
            else:
                output.append(prevWindowMax)
        
        for r in range(k - 1, len(nums)):
            if k == 1:
                window = nums[l]
                output.append(window)
            else:
                window = nums[l : r + 1]
                curr_max = max(window)
                if l == 0:
                    output.append(curr_max)
                else:
                    maxSlidingWindowHelper(curr_max, nums[r])
            
            l += 1

        return output

