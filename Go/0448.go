func findDisappearedNumbers(nums []int) []int {
    n := len(nums)

    for i := 0; i < n; i++ {
        newIndex := abs(nums[i]) - 1
        if nums[newIndex] > 0 {
            nums[newIndex] *= -1
        }
    }

    res := []int{}
    for i := 1; i <= n; i++ {
        if nums[i - 1] > 0 {
            res = append(res, i)
        }
    }

    return res
}

func abs(x int) int {
    if x < 0 {
        return -x
    }

    return x
}
