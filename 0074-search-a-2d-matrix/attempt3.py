class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows_l = 0
        rows_r = len(matrix) - 1
        
        while rows_l <= rows_r:
            rows_m = (rows_l + rows_r) // 2

            if matrix[rows_m][0] > target:
                rows_r = rows_m - 1
            elif matrix[rows_m][len(matrix[rows_m]) - 1] < target:
                rows_l = rows_m + 1
            else:
                l = 0
                r = len(matrix[rows_m]) - 1
                while l <= r:
                    m = (l + r) // 2
                    if matrix[rows_m][m] == target:
                        return True
                    elif matrix[rows_m][m] < target:
                        l = m + 1
                    elif matrix[rows_m][m] > target:
                        r = m - 1
                return False

