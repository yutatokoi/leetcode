#include <string.h>

int palindrome(char* s, int l, int r);

bool validPalindrome(char* s) {
    int l = 0, r = strlen(s) - 1;
    while (l < r) {
        if (s[l] != s[r]) {
            return (palindrome(s, l + 1, r) || palindrome(s, l, r - 1));
        }
        l++;
        r--;
    }

    return 1;
}

int palindrome(char* s, int l, int r) {
    while (l < r) {
        if (s[l] != s[r]) {
            return 0;
        }
        l++;
        r--;
    }

    return 1;
}
