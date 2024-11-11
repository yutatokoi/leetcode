func islandPerimeter(grid [][]int) int {
    islands := 0
    neighbors := 0

    for r := 0; r < len(grid); r++ {
        for c := 0; c < len(grid[0]); c++ {
            if grid[r][c] == 1 {
                islands++
                if r - 1 >= 0 && grid[r - 1][c] == 1 {
                    neighbors++
                }
                if c - 1 >= 0 && grid[r][c - 1] == 1 {
                    neighbors++
                }
            }
        }
    }

    return islands * 4 - neighbors * 2
}
