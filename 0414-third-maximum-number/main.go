// attempt1 (using HashSet)
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

// attempt2 (without HashSet)
import "sort"

func thirdMax(nums []int) int {
    sort.Slice(nums, func(i, j int) bool {
        return nums[i] > nums[j]
    })
    
    n := len(nums)
    ans := nums[0]
    elemCount := 1
    for i := 1; i < n; i++ {
        if nums[i] != ans {
            ans = nums[i]
            elemCount++
        }

        if elemCount == 3 {
            break
        }
    }

    if elemCount == 3 {
        return ans
    }

    return nums[0]
}
