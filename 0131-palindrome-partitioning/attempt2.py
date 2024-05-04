class Solution:
    def partition(self, s: str) -> List[List[str]]:
        output = []
        sub = []

        def backtrack(i):
            if i >= len(s):
                output.append(sub.copy())
                return
            for j in range(i, len(s)):
                if self.isPalindrome(s, i, j):
                    sub.append(s[i:j + 1])
                    backtrack(j + 1)
                    sub.pop()

        backtrack(0)
        return output
            
    def isPalindrome(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True


