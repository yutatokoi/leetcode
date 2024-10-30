import (
    "strings"
    "unicode"
)

func licenseKeyFormatting(s string, k int) string {
    s = strings.ReplaceAll(s, "-", "")
    s = strings.ToUpper(s)

    if len(s) == 0 {
        return ""
    }

    formatted := ""
    count := 0

    for i:= len(s) - 1; i >= 0; i-- {
        if unicode.IsLetter(rune(s[i])) || unicode.IsDigit(rune(s[i])) {
            if count == k {
                formatted = "-" + formatted
                count = 0
            }

            formatted = string(s[i]) + formatted
            count++
        }
    }

    return formatted
}
