func findMaxConsecutiveOnes(nums []int) int {
    max := 0
    i := 0
    for i < len(nums) {
        curr := 0
        for i < len(nums) && nums[i] == 1 {
            curr++
            if curr > max {
                max = curr
            }
            i++
        }
        i++
    }

    return max
}
