#include <string.h>

int countSegments(char* s) {
    int segments = 0;
    int ln = strlen(s);

    for (int i = 0; i < ln; i++) {
        if ((i == 0 || s[i - 1] == ' ') && (s[i] != ' ')) {
            segments++;
        }
    }

    return segments;
}
