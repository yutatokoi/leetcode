/**
 * Note: The returned array must be malloced, assume caller calls free().
 */

#include <stdio.h>

int* findErrorNums(int* nums, int numsSize, int* returnSize) {
    int count[numsSize + 1] = {};
    int duplicate = 0, missing = 0;

    for (int i = 0; i < numsSize; i++) {
        count[nums[i]] += 1;
    }

    for (int i = 1; i < numsSize + 1; i++) {
        if (count[i] == 2) duplicate = i;
        if (count[i] == 0) missing = i;
    }

    int *ans = malloc(2 * sizeof(int));
    ans[0] = duplicate;
    ans[1] = missing;
    *returnSize = 2;

    return ans;
}
