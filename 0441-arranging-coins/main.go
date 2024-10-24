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
