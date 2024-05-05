class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        num_letter_dict = {'2': ('a', 'b', 'c'), '3': ('d', 'e', 'f'), '4': ('g', 'h', 'i'), '5': ('j', 'k', 'l'), '6': ('m', 'n', 'o'), '7': ('p', 'q', 'r', 's'), '8': ('t', 'u', 'v'), '9': ('w', 'x', 'y', 'z')}

        res = []

        def backtrack(i, combination):
            if len(combination) == len(digits):
                res.append(combination)
                return

            for c in num_letter_dict[digits[i]]:
                backtrack(i + 1, combination + c)

        if digits:
            backtrack(0, "")

        return res
        

