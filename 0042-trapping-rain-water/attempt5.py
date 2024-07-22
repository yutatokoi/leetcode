class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        l_max, r_max = height[l], height[r]
        total = 0

        while l < r:
            if l_max <= r_max:
                total += l_max - height[l]
                l += 1
                l_max = max(l_max, height[l])
            else:
                total += r_max - height[r]
                r -= 1
                r_max = max(r_max, height[r])

        return total


