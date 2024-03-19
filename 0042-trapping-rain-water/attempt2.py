class Solution:
    def trap(self, height: List[int]) -> int:
        result = 0
        max_left = []
        max_right = []
        for i in range(len(height)):
            if i == 0:
                max_left.append(0)
            else:
                max_left.append(max(max_left[i - 1], height[i]))
        height.reverse()
        for i in range(len(height)):
            if i == 0:
                max_right.append(0)
            else:
                max_right.append(max(max_right[i - 1], height[i]))
        height.reverse()
        max_right.reverse()
        for i in range(len(height)):
            if (min(max_left[i], max_right[i]) - height[i] < 0):
                continue
            else:
                result += (min(max_left[i], max_right[i]) - height[i])
        return result

