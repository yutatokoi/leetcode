#include <string.h>

int isUpper(char ch);

int longestPalindrome(char* s) {
    int pairs = 0, n = strlen(s);
    int count[52] = {0};

    for (int i = 0; i < n; i++) {
        int index;
        if (isUpper(s[i])) {
            index = s[i] - 'A' + 26;
        } else {
            index = s[i] - 'a';
        }
        count[index]++;

        if (count[index] % 2 == 0) {
            pairs++;
        }
    }

    if (pairs * 2 == n) {
        return n;
    }

    return pairs * 2 + 1;
}

int isUpper(char ch) {
    if ('a' <= ch && ch <= 'z') {
        return 0;
    } else {
        return 1;
    }
}
