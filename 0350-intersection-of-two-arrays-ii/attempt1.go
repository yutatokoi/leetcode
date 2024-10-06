func intersect(nums1 []int, nums2 []int) []int {
    seen := make([]int, 1001)

    for _, n := range nums1 {
        seen[n]++
    }

    res := []int{}

    for _, n := range nums2 {
        if seen[n] > 0 {
            res = append(res, n)
            seen[n]--
        }
    }

    return res
}
