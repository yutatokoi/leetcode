import "slices"

func topKFrequent(nums []int, k int) []int {
    counts := make(map[int]int)

    for _, n := range nums {
        counts[n]++
    }

    var frequencies [][]int
    for n, count := range counts {
        frequencies = append(frequencies, []int{count, n})
    }
    
    slices.SortFunc(frequencies, func (a, b []int) int {
        return b[0] - a[0]
    })

    output := make([]int, k)
    for i := 0; i < k; i++ {
        output[i] = frequencies[i][1]
    }

    return output
}
