import "sort"

func thirdMax(nums []int) int {
    uniqueNums := make(map[int]bool)
    for _, n := range nums {
        uniqueNums[n] = true
    }

    slice := make([]int, 0, len(uniqueNums))
    for n := range uniqueNums {
        slice = append(slice, n)
    }

    sort.Slice(slice, func(i, j int) bool {
        return slice[i] > slice[j]
    })

    if len(slice) < 3 {
        return slice[0]
    }

    return slice[2]
}
