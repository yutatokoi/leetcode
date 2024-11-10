class Solution:
    def addBinary(self, a: str, b: str) -> str:
        s = []
        curr_sum = 0
        i = len(a) - 1
        j = len(b) - 1

        while (i >= 0) or (j >= 0) or curr_sum:
            if i >= 0:
                curr_sum += int(a[i])
                i -= 1
            if j >= 0:
                curr_sum += int(b[j])
                j -= 1
            s.append(str(curr_sum % 2))
            curr_sum //= 2

        return "".join(reversed(s))
        
        
