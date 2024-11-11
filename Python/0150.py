class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t in "+-*/":
                res = str(int(eval(f'{stack[-2]} {t} {stack[-1]}')))
                stack = stack[:-2]
                stack.append(res)
            else:
                stack.append(t)

        return int(stack.pop())


