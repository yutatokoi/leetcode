class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for bracket in s:
            if bracket in "([{":
                stack.append(bracket)
            elif not stack:
                return False
            elif bracket == ")" and not stack.pop() == "(":
                return False
            elif bracket == "]" and not stack.pop() == "[":
                return False
            elif bracket == "}" and not stack.pop() == "{":
                return False

        return not stack

        
