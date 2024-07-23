class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        pos_speed = []

        for i in range(len(position)):
            pos_speed.append((position[i], speed[i]))

        pos_speed = sorted(pos_speed)[::-1]

        for p, s in pos_speed:
            time = (target - p) / s
            stack.append(time)

            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)

        
