class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        license_plate_letters = [0] * 26
        for ch in licensePlate:
            if ch.isalpha():
                license_plate_letters[ord(ch.lower()) - ord('a')] += 1

        # (bool is_complete, word_len)
        complete_words = []
        minimum_length = 16
        for word in words:
            word_len = len(word)
            word_letters = [0] * 26
            for ch in word:
                if ch.isalpha():
                    word_letters[ord(ch.lower()) - ord('a')] += 1
            
            complete = True
            for i in range(len(word_letters)):
                if word_letters[i] < license_plate_letters[i]:
                    complete = False
                    break

            complete_words.append((complete, word_len))
            if complete:
                minimum_length = min(minimum_length, word_len)

        ans = 0
        for i in range(len(complete_words)):
            if complete_words[i][0] and complete_words[i][1] == minimum_length:
                ans = i
                break

        return words[ans]
