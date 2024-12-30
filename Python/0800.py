class Solution:
    def similarRGB(self, color: str) -> str:
        def find_target(color_section):
            num = int(color_section, 16)
            x = round(num / 17)
            return hex(x)[-1] * 2

        target_color = "#"
        for i in range(1, 6, 2):
            target_color += find_target(color[i:i + 2])

        return target_color
