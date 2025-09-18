func isAnagram(s string, t string) bool {
    if len(s) != len(t) {
        return false
    }

    const ALPHABET_LENGTH = 26
    chars := make([]int, ALPHABET_LENGTH)

    for _, r := range s {
        chars[int(r) - int('a')]++
    }
    for _, r := range t {
        chars[int(r) - int('a')]--
    }

    for i := 0; i < ALPHABET_LENGTH; i++ {
        if chars[i] != 0 {
            return false
        }
    }

    return true
}
