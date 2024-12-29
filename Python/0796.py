class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        length = len(s)
        for i in range(length):
            if (s[i:length] + s[:i] == goal):
                return True

        return False
