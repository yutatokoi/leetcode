class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])

        path = set()

        def dfs(r, c, i):
            if i == len(word):
                return True

            if r < 0 or c < 0 or r >= ROWS or c >= COLS:
                return False
            if word[i] != board[r][c]:
                return False
            if (r, c) in path:
                return False

            path.add((r, c))

            i += 1
            res = (dfs(r + 1, c, i) or
                    dfs(r - 1, c, i) or
                    dfs(r, c + 1, i) or
                    dfs(r, c - 1, i))

            path.remove((r, c))
            return res

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True

        return False
            


