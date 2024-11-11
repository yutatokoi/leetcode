// attempt1 create rows
func arrangeCoins(n int) int {
    rows := 0
    i := 1

    for n >= i {
        n -= i
        i++
        rows++
    }

    return rows
}

// attempt2 single calculation
import "math"

func arrangeCoins(n int) int {
    return (int)(-1 + math.Sqrt((float64)(1 + 8 * n))) / 2
}
