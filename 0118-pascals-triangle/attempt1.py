class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
         
        for i in range(numRows - 1):
            prev_row = [0] + res[-1] + [0]
            new_row = []
            for j in range(len(res[-1]) + 1):
                new_row.append(prev_row[j] + prev_row[j + 1])
            res.append(new_row)

        return res
        

