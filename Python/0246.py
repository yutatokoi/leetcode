class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        matching = {
            "0": "0",
            "1": "1",
            "2": "no",
            "3": "no",
            "4": "no",
            "5": "no",
            "6": "9",
            "7": "no",
            "8": "8",
            "9": "6"
        }

        if len(num) == 1:
            return matching[num[0]] == num[0]

        l = 0
        r = len(num) - 1
        
        while l <= r:
            if matching[num[l]] != num[r]:
                return False

            l += 1
            r -= 1

        return True

        
