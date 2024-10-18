/**
 * Note: The returned array must be malloced, assume caller calls free().
 */

#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <string.h>

char** fizzBuzz(int n, int* returnSize) {
    char **res = malloc(sizeof(char *) * n);
    assert(res != NULL);
    *returnSize = n;

    for (int i = 1; i <= n; i++) {
        if (i % 15 == 0) {
            res[i - 1] = malloc(strlen("FizzBuzz") + 1);
            strcpy(res[i - 1], "FizzBuzz");
        } else if (i % 3 == 0) {
            res[i - 1] = malloc(strlen("Fizz") + 1);
            strcpy(res[i - 1], "Fizz");
        } else if (i % 5 == 0) {
            res[i - 1] = malloc(strlen("Buzz") + 1);
            strcpy(res[i - 1], "Buzz");
        } else {
            res[i - 1] = malloc(5);
            sprintf(res[i - 1], "%d", i);
        }
    }

    return res;
}
