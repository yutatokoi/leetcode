func intersection(nums1 []int, nums2 []int) []int {
    seen := make([]int, 1001)
    for _, n := range nums1 {
        seen[n]++
    }

    res := make([]int, 0)
    for _, n := range nums2 {
        if seen[n] > 0 {
            res = append(res, n)
            seen[n] = 0
        }
    }

    return res
}
