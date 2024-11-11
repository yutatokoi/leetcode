class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0

        for i, height in enumerate(heights):
            start = i
            while stack and stack[-1][1] > height:
                j, prev_height = stack.pop()
                max_area = max(max_area, prev_height * (i - j))
                start = j

            stack.append((start, height))

        for i, height in stack:
            max_area = max(max_area, height * (len(heights) - i))

        return max_area


