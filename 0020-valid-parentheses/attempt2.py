class Solution:
    def isValid(self, s: str) -> bool:
        bracket_dict = {')' : '(', ']' : '[', '}' : '{'}
        bracket_stack = []

        for c in s:
            if c in bracket_dict:
                if bracket_stack and (bracket_stack[-1] == bracket_dict[c]):
                    bracket_stack.pop()
                else:
                    return False
            else:
                bracket_stack.append(c)

        if not bracket_stack:
            return True
        else:
            return False

