#include <string.h>

int min(int a, int b);

int countBinarySubstrings(char* s) {
    int ans = 0, prev = 0, curr = 1;
    int n = strlen(s);

    for (int i = 1; i < n; i++) {
        if (s[i - 1] != s[i]) {
            ans += min(prev, curr);
            prev = curr;
            curr = 1;
        } else {
            curr++;
        }
    }

    return ans + min(prev, curr);
}

int min(int a, int b) {
    if (a < b) {
        return a;
    }

    return b;
}
