#include <string.h>

bool checkRecord(char* s) {
    int i = 0, absence = 0, n = strlen(s);

    while (i < n) {
        if (s[i] == 'A') {
            absence++;
            if (absence == 2) {
                return 0;
            }
            i++;
        } else if (s[i] == 'L') {
            int consecutiveLate = 1;
            i++;
            while (i < n && s[i] == 'L') {
                consecutiveLate++;
                i++;
            }
            if (consecutiveLate >= 3) {
                return 0;
            }
        } else {
            i++;
        }
    }

    return 1;
}
