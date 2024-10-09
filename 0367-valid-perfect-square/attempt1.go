func isPerfectSquare(num int) bool {
    left, right := 0, num + 1

    for (left < right) {
        mid := left + (right - left) / 2

        if mid * mid >= num {
            right = mid
        } else {
            left = mid + 1
        }
    }

    return left * left == num
}
