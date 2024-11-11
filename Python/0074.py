class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1

        while l <= r:
            m = (l + r) // 2
            if matrix[m][0] <= target <= matrix[m][len(matrix[m]) - 1]:
                row_l, row_r = 0, len(matrix[m])
                while row_l <= row_r:
                    row_m = (row_l + row_r) // 2
                    if matrix[m][row_m] == target:
                        return True
                    elif matrix[m][row_m] < target:
                        row_l = row_m + 1
                    elif matrix[m][row_m] > target:
                        row_r = row_m - 1
                break
            elif matrix[m][0] > target:
                r = m - 1
            elif matrix[m][len(matrix[m]) - 1] < target:
                l = m + 1

        return False

        
