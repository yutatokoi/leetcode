import "sort"

func findContentChildren(g []int, s []int) int {
    sort.Ints(g)
    sort.Ints(s)

    contentChildren := 0
    cookieIndex := 0
    for cookieIndex < len(s) && contentChildren < len(g) {
        if s[cookieIndex] >= g[contentChildren] {
            contentChildren++
        }
        cookieIndex++
    }

    return contentChildren
}
