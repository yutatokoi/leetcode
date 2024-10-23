import "strings"

func countSegments(s string) int {
    words := strings.Fields(s)

    return len(words)    
}
