class Solution:
    def trap(self, height: List[int]) -> int:
        result = 0
        l = 0
        r = 1
        while r < len(height):
            if height[l] > height[r]:
                r += 1    
            if height[l] <= height[r]:
                area = (r - l) * min(height[l], height[r])
                while l < r:
                    area -= height[l]
                    l += 1
                result += area
            r += 1
        return result

