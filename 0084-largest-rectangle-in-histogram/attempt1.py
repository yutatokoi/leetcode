class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        areas = []
        for i in range(len(heights)):
            width = 1
            l = i - 1
            r = i + 1
            while l >= 0 and heights[l] >= heights[i]:
                width += 1
                l -= 1
            while r < len(heights) and heights[r] >= heights[i]:
                width += 1
                r += 1
            area = heights[i] * width
            areas.append(area)
        return max(areas)
        
