class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows_l = 0
        rows_r = len(matrix) - 1
        
        while rows_l <= rows_r:
            l = 0
            r = len(matrix[rows_l]) - 1

            while l <= r:
                m = (r + l) // 2

                if matrix[rows_l][m] == target:
                    return True
                elif matrix[rows_l][m] < target:
                    l = m + 1
                elif matrix[rows_l][m] > target:
                    r = m - 1
                
                if matrix[rows_r][m] == target:
                    return True
                elif matrix[rows_r][m] < target:
                    l = m + 1
                elif matrix[rows_r][m] > target:
                    r = m - 1
                
            rows_m = (rows_l + rows_r) // 2
            rows_l = m + 1
            rows_r = m - 1
        
        return False
    
