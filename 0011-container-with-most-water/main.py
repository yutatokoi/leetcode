class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_container = 0

        while l < r:
            curr_container = (r - l) * min(height[l], height[r])
            max_container = max(max_container, curr_container)

            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1

        return max_container

        
