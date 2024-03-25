class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        areas = []
        for i in range(len(heights)):
            width = 1
            j = i + 1
            while j < len(heights) and heights[j] >= heights[i]:
                width += 1
                j += 1
            area = heights[i] * width
            areas.append(area)
        return max(areas)

