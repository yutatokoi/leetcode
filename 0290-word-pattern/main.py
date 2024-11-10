class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False

        letter_to_word = dict()
        for i in range(len(pattern)):
            letter = pattern[i]

            if letter in letter_to_word and words[i] != letter_to_word[letter]:
                return False
            else:
                letter_to_word[letter] = words[i]

        word_to_letter = dict()
        for i in range(len(words)):
            word = words[i]

            if word in word_to_letter and pattern[i] != word_to_letter[word]:
                return False
            else:
                word_to_letter[word] = pattern[i]

        return True

        
