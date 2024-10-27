func hammingDistance(x int, y int) int {
    distance := 0
    z := x ^ y
    for z > 0 {
        remainder := z % 2
        if remainder == 1 {
            distance++
        }
        z /= 2
    }
    return distance
}
