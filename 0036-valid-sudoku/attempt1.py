class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows_valid = True
        for r in board:
            row_set = set()
            for i in r:
                if i == '.':
                    rows_valid = rows_valid
                elif i in row_set:
                    rows_valid = False
                else:
                    row_set.add(i)

        columns_valid = True
        for i in range(9):
            col_set = set()
            for j in range(9):
                if board[j][i] == '.':
                    columns_valid = columns_valid
                elif board[j][i] in col_set:
                    columns_valid = False
                else:
                    col_set.add(board[j][i])

        subboxes_valid = True
        for row in range(0, 3):
            box_set = set()
            for i in range(0, 3):
                if board[row][i] == '.':
                    subboxes_valid = subboxes_valid
                elif board[row][i] in box_set:
                    subboxes_valid = False
                else:
                    box_set.add(board[row][i])
        
            box_set = set()
            for i in range(3, 6):
                if board[row][i] == '.':
                    subboxes_valid = subboxes_valid
                elif board[row][i] in box_set:
                    subboxes_valid = False
                else:
                    box_set.add(board[row][i])
        
            box_set = set()
            for i in range(6, 9):
                if board[row][i] == '.':
                    subboxes_valid = subboxes_valid
                elif board[row][i] in box_set:
                    subboxes_valid = False
                else:
                    box_set.add(board[row][i])

        for row in range(3, 6):
            box_set = set()
            for i in range(0, 3):
                if board[row][i] == '.':
                    subboxes_valid = subboxes_valid
                elif board[row][i] in box_set:
                    subboxes_valid = False
                else:
                    box_set.add(board[row][i])

            box_set = set()
            for i in range(3, 6):
                if board[row][i] == '.':
                    subboxes_valid = subboxes_valid
                elif board[row][i] in box_set:
                    subboxes_valid = False
                else:
                    box_set.add(board[row][i])

            box_set = set()
            for i in range(6, 9):
                if board[row][i] == '.':
                    subboxes_valid = subboxes_valid
                elif board[row][i] in box_set:
                    subboxes_valid = False
                else:
                    box_set.add(board[row][i])

        for row in range(6, 9):
            box_set = set()
            for i in range(0, 3):
                if board[row][i] == '.':
                    subboxes_valid = subboxes_valid
                elif board[row][i] in box_set:
                    subboxes_valid = False
                else:
                    box_set.add(board[row][i])

            box_set = set()
            for i in range(3, 6):
                if board[row][i] == '.':
                    subboxes_valid = subboxes_valid
                elif board[row][i] in box_set:
                    subboxes_valid = False
                else:
                    box_set.add(board[row][i])

            box_set = set()
            for i in range(6, 9):
                if board[row][i] == '.':
                    subboxes_valid = subboxes_valid
                elif board[row][i] in box_set:
                    subboxes_valid = False
                else:
                    box_set.add(board[row][i])

        return rows_valid and columns_valid and subboxes_valid

