#include <string.h>

bool isSubsequence(char* s, char* t) {
    int i = 0, j = 0;

    while (i < strlen(s) && j < strlen(t)) {
        if (s[i] == t[j]) {
            i++;
        }
        j++;
    }

    return i == strlen(s);
}
