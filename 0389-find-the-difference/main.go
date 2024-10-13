func findTheDifference(s string, t string) byte {
    sCount := make([]int, 26)

    for i := 0; i < len(s); i++ {
        sCount[int(s[i]) - int('a')]++
    }

    var index int
    for index = 0; index < len(t); index++ {
        sCount[int(t[index]) - int('a')]--
        if sCount[int(t[index]) - int('a')] < 0 {
            break
        }
    }

    return t[index]
}
