#include <string.h>

char findTheDifference(char* s, char* t) {
    int sCount[26] = {0};
    
    int sLen = strlen(s);
    for (int i = 0; i < sLen; i++) {
        sCount[s[i] - 'a']++;
    }

    int tLen = strlen(t), index;
    for (index = 0; index < tLen; index++) {
        sCount[t[index] - 'a']--;

        if (sCount[t[index] - 'a'] < 0) {
            break;
        }
    }

    return t[index];
}
