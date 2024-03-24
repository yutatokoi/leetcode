class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t == '+':
                stack.append(str(eval(f'{stack[-2]} + {stack[-1]}')))
                stack.pop(-3)
                stack.pop(-2)
            elif t == '-':
                stack.append(str(eval(f'{stack[-2]} - {stack[-1]}')))
                stack.pop(-3)
                stack.pop(-2)    
            elif t == '*':
                stack.append(str(eval(f'{stack[-2]} * {stack[-1]}')))
                stack.pop(-3)
                stack.pop(-2)
            elif t == '/':
                stack.append(str(int(eval(f'{stack[-2]} / {stack[-1]}'))))
                stack.pop(-3)
                stack.pop(-2)
            else:
                stack.append(t)
        return int(stack[-1])

