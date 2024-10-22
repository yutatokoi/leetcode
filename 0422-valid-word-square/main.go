func validWordSquare(words []string) bool {
    for r, ln := 0, len(words); r < ln; r++ {
        for c := 0; c < len(words[r]); c++ {
            if c >= ln || r >= len(words[c]) || words[r][c] != words[c][r] {
                return false
            }
        }
    }

    return true
}
