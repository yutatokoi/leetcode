#include <string.h>

void reverseWord(char *start, char *end);

char* reverseWords(char* s) {
    int len = strlen(s);
    char *start = s;

    for (int i = 0; i <= len; i++) {
        if (s[i] == ' ' || s[i] == '\0') {
            reverseWord(start, &s[i - 1]);
            start = &s[i + 1];
        }
    }

    return s;
}

void reverseWord(char *start, char *end) {
    char temp;
    while (start < end) {
        temp = *start;
        *start = *end;
        *end = temp;
        start++;
        end--;
    }
}
