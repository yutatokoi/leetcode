class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """

        rows = len(rooms)
        cols = len(rooms[0])

        def bfs(r, c):
            q = collections.deque()
            q.append((r, c))

            while q:
                row, col = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (r in range(rows) and 
                        c in range(cols) and
                        grid[r][c] == 0)

        for r in range(rows):
            for c in range(cols):
                if rooms[r][c] == -1 or rooms[r][c] == 0:
                    break
                elif rooms[r][c] == 2147483647:
                    rooms[r][c] == bfs(r, c)

        return
        
