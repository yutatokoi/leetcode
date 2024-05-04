class Solution:
    def partition(self, s: str) -> List[List[str]]:
        output = []

        def backtrack(i, j):
            sub = []
            while i <= j:
                if s[i:j] == s[j:i:-1]:
                    sub.append(s[i:j])
                j -= 1

            sub.append(output)

        for i in range(len(s)):
            backtrack(i, len(s) - 1)

        return output
        
