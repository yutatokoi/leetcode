#include <string.h>

int firstUniqChar(char* s) {
    int counts[26] = {0};

    int len = strlen(s);
    for (int i = 0; i < len; i++) {
        counts[s[i] - 'a']++;
    }

    for (int i = 0; i < len; i++) {
        if (counts[s[i] - 'a'] == 1) {
            return i;
        }
    }

    return -1;
}
