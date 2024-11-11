func validWordAbbreviation(word string, abbr string) bool {
    n, m, i, j := len(word), len(abbr), 0, 0

    for i < n && j < m {
        if word[i] == abbr[j] {
            i++
            j++
        } else if abbr[j] >= '0' && abbr[j] <= '9' {
            c := 0
            for j < m && abbr[j] >= '0' && abbr[j] <= '9' {
                c *= 10
                d := int(abbr[j] - '0')
                if c == 0 && d == 0 {
                    return false
                } else {
                    c += d
                }
                j++
            }

            if i + c <= n {
                i += c
            } else {
                return false
            }

        } else {
            return false
        }
    }

    return i == n && j == m
}
