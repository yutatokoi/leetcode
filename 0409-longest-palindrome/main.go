// attempt1 (HashMap)
func longestPalindrome(s string) int {
    pairs := 0
    count := map[rune]int{}

    for _, ch := range s {
        count[ch]++
        if count[ch] % 2 == 0 {
            pairs++
        }
    }

    if pairs * 2 == len(s) {
        return len(s)
    }

    return pairs * 2 + 1
}
