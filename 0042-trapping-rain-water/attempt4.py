class Solution:
    def trap(self, height: List[int]) -> int:
        result = 0
        l = 0
        r = len(height) - 1
        lmax = height[l]
        rmax = height[r]

        while l < r:
            if lmax < rmax:
                l += 1
                lmax = max(lmax, height[l])
                result += lmax - height[l]
            else:
                r -= 1
                rmax = max(rmax, height[r])
                result += rmax - height[r]

        return result

