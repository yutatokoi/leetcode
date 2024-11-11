import math

class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        ans = [area, 1]

        for width in range(1, int(math.sqrt(area) + 1)):
            if area % width == 0:
                ans = [area // width, width]

        return ans
