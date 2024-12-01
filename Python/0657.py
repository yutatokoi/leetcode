class Solution:
    def judgeCircle(self, moves: str) -> bool:
        position = [0, 0]

        for move in moves:
            if move == 'U':
                position[1] += 1
            if move == 'D':
                position[1] -= 1
            if move == 'R':
                position[0] += 1
            if move == 'L':
                position[0] -= 1

        return position == [0, 0]
