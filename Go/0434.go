// attempt1 (built-in function)
import "strings"

func countSegments(s string) int {
    words := strings.Fields(s)

    return len(words)    
}

// attempt2 O(1) extra space, O(n) time
func countSegments(s string) int {
    segments := 0

    for i := 0; i < len(s); i++ {
        if (i == 0 || s[i - 1] == ' ') && (s[i] != ' ') {
            segments++
        }
    }

    return segments
}
