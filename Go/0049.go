const ALPHABET_SIZE = 26

func groupAnagrams(strs []string) [][]string {
    anagrams := make(map[[ALPHABET_SIZE]int][]string)

    for _, s := range strs {
        chars := characters(s)
        anagrams[chars] = append(anagrams[chars], s)
    }

    res := [][]string{}
    for _, anagram := range anagrams {
        res = append(res, anagram)
    }
    return res
}

func characters(s string) [ALPHABET_SIZE]int {
    chars := [ALPHABET_SIZE]int{}

    for _, ch := range s {
        chars[int(ch) - int('a')]++
    }
    return chars
}
