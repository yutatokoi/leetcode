class Solution:
    def checkRecord(self, s: str) -> bool:
        absence = 0
        i = 0
        n = len(s)

        while i < n:
            if s[i] == 'A':
                absence += 1
                if absence == 2:
                    return False
                i += 1
            elif s[i] == 'L':
                consecutiveLate = 1
                i += 1
                while i < n and s[i] == 'L':
                    consecutiveLate += 1
                    i += 1
                if consecutiveLate >= 3:
                    return False
            else:
                i += 1

        return True
