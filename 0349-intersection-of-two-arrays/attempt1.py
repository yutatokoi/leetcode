func intersection(nums1 []int, nums2 []int) []int {
    res := []int{}

    // nums1 is set to the shorter slice
    if len(nums1) > len(nums2) {
        nums1, nums2 = nums2, nums1
    }

    for _, n := range nums2 {
        intersects := false
        for _, m := range nums1 {
            if n == m {
                intersects = true
            }
        }

        isDuplicate := false
        for _, o := range res {
            if n == o {
                isDuplicate = true
            }
        }

        if intersects && !isDuplicate {
            res = append(res, n)
        }
    }

    return res
}
