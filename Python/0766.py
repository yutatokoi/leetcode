class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        # Check diagonals that start from top row
        for r in range(rows):
            c = 0
            val = matrix[r][c]
            
            r += 1
            c += 1
            while c < cols and r < rows:
                if matrix[r][c] != val:
                    return False
                r += 1
                c += 1
        
        # Check diagonals that start from left col
        for c in range(cols):
            r = 0
            val = matrix[r][c]
            
            r += 1
            c += 1
            while r < rows and c < cols:
                if matrix[r][c] != val:
                    return False
                r += 1
                c += 1

        return True
