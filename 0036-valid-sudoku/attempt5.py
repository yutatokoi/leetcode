class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Rows
        for row in board:
            row_set = set()
            for num in row:
                if num == ".":
                    continue
                if num in row_set:
                    return False
                row_set.add(num)

        # Cols
        cols = collections.defaultdict(set)
        for r in range(len(board)):
            for c in range(len(board[0])):
                num = board[r][c]
                if num == ".":
                    continue
                if num in cols[c]:
                    return False
                cols[c].add(num)
        
        # Sub-boxes
        boxes = collections.defaultdict(set)
        for r in range(len(board)):
            for c in range(len(board)):
                num = board[r][c]
                if num == ".":
                    continue
                r_id = r // 3
                c_id = c // 3
                if num in boxes[(r_id, c_id)]:
                    return False
                boxes[(r_id, c_id)].add(num)

        return True

        
