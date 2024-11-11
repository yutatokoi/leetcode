// attempt1 create rows
int arrangeCoins(int n) {
    int rows = 0, i = 1;

    while (n >= i) {
        n -= i;
        i++;
        rows++;
    }

    return rows;
}

// attempt2 single calculation
#include <math.h>

int arrangeCoins(int n) {
    return (int)(-1 + sqrt(1 + 8.0 * n)) / 2;
}
