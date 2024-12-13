#include <string.h>

char* toLowerCase(char* s) {
    int len = strlen(s);

    for (int i = 0; i < len; i++) {
        if ('A' <= s[i] && s[i] <= 'Z') {
            s[i] = s[i] - 'A' + 'a';
        }
    }

    return s;
}
