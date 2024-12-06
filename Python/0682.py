class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []

        for op in operations:
            if (op.isnumeric() or (op[0] == '-' and op[1:].isnumeric())):
                record.append(int(op))
            elif op == '+':
                record.append(record[-1] + record[-2])
            elif op == 'D':
                record.append(2 * record[-1])
            elif op == 'C':
                record.pop()

            print(record)

        return sum(record)
