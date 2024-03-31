class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_letters = dict()
        for c in s1:
            if c in s1_letters:
                s1_letters[c] += 1
            else:
                s1_letters[c] = 1
        
        for i in range(len(s2)):
            s2_substring = s2[i : i + len(s1)]
            s2_substring_letters = dict()
            for c in s2_substring:
                if c in s2_substring_letters:
                    s2_substring_letters[c] += 1
                else:
                    s2_substring_letters[c] = 1
            for key in s1_letters.keys():
                if key in s2_substring_letters and s1_letters[key] == s2_substring_letters[key]:
                    s2_substring_letters[key] = 0
            value_sum = 0
            for value in s2_substring_letters.values():
                value_sum += value
            if value_sum == 0:
                return True
            else:
                continue

        return False

