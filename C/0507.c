#include <math.h>

bool checkPerfectNumber(int num) {
    if (num % 2 == 1) return 0;

    int total = 0;
    int n = ceil(sqrt(num));
    for (int i = 1; i < n; i++) {
        if (num % i == 0) {
            total += i;
            total += num / i;
        }
    }

    return total / 2 == num;
}
