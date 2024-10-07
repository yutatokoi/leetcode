func minLength(s string) int {
    i := 0
    for (i < len(s) - 1) {
        if (s[i] == 'A' && s[i+1] == 'B') {
            s = s[:i] + s[i+2:]
            i = 0
            continue
        }

        if (s[i] == 'C' && s[i+1] == 'D') {
            s = s[:i] + s[i+2:]
            i = 0
            continue
        }

        i++
    }

    return len(s)
}
