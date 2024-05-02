class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        height = len(board)
        width = len(board[0])

        word = list(word)

        cur = []

        t = 0
        while t < height * width ** 2:
            def backtrack(cur, row, col, i):
                if cur == word:
                    return True

                if row < 0 or col < 0 or row >= height or col >= width:
                    return False

                if board[row][col] == word[i]:
                    cur.append(board[row][col])
                    i += 1

                return (backtrack(cur, row + 1, col, i) or
                        backtrack(cur, row, col + 1, i) or
                        backtrack(cur, row - 1, col, i) or
                        backtrack(cur, row, col - 1, i))
            t += 1

