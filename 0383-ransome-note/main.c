#include <string.h>

bool canConstruct(char* ransomNote, char* magazine) {
    int magazineLetters[26] = {0};
    int len = strlen(magazine);

    for (int i = 0; i < len; i++) {
        magazineLetters[magazine[i] - 'a']++;
    }

    len = strlen(ransomNote);
    for (int i = 0; i < len; i++) {
        magazineLetters[ransomNote[i] - 'a']--;

        if (magazineLetters[ransomNote[i] - 'a'] < 0) {
            return false;
        }
    }

    return true;
}
