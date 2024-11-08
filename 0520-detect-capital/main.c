#include <string.h>
#include <ctype.h>

bool detectCapitalUse(char* word) {
    int len = strlen(word);
    if (len == 1) return 1;

    if (islower(word[0])) {
        for (int i = 1; i < len; i++) {
            if (isupper(word[i])) return 0;
        }
    } else if (isupper(word[1])) {
        for (int i = 2; i < len; i++) {
            if (islower(word[i])) return 0;
        }
    } else if (islower(word[1])) {
        for (int i = 2; i < len; i++) {
            if (isupper(word[i])) return 0;
        }
    }

    return 1;
}
