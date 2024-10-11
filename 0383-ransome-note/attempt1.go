func canConstruct(ransomNote string, magazine string) bool {
    var magazineLetters = [26]int{}

    for _, ch := range magazine {
        magazineLetters[int(ch) - int('a')]++
    }

    for _, ch := range ransomNote {
        magazineLetters[int(ch) - int('a')]--
        if magazineLetters[int(ch) - int('a')] < 0 {
            return false
        }
    }

    return true
}
