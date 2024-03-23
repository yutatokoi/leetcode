class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ['+', '-', '*', '/']
        for o in tokens:
            if o in operators:
                result = eval(f'{stack.pop(-2)} {o} {stack.pop(-1)}')
                if o != '/':
                    stack.append(str(result))
                else:
                    stack.append(str(int(result)))

            else:
                stack.append(o)
            
        return int(stack[-1])

