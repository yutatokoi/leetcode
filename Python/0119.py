class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        pascal = [[1]]

        for i in range(1, rowIndex + 1):
            prev_row = [0] + pascal[-1] + [0]
            curr_row = []

            for j in range(len(prev_row) - 1):
                curr_row.append(prev_row[j] + prev_row[j + 1])

            pascal.append(curr_row)

        return pascal[-1]
        
