#include <string.h>

int findLUSlength(char* a, char* b) {
    if (strcmp(a, b) == 0) return -1;

    return max(strlen(a), strlen(b));
}

int max(int n, int m) {
    if (n > m) {
        return n;
    }

    return m;
}
