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

// attempt2 (array)
import "unicode"

func longestPalindrome(s string) int {
    pairs := 0
    count := make([]int, 52)

    for _, ch := range s {
        var index int
        if unicode.IsUpper(ch) {
            index = int(ch) - int('A') + 26
        } else {
            index = int(ch) - int('a')
        }
        count[index]++

        if count[index] % 2 == 0 {
            pairs++
        }
    }

    if pairs * 2 == len(s) {
        return len(s)
    }

    return pairs * 2 + 1
}
