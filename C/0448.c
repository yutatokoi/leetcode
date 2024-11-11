/**
 * Note: The returned array must be malloced, assume caller calls free().
 */

#include <stdlib.h>

int* findDisappearedNumbers(int* nums, int numsSize, int* returnSize) {
    for (int i = 0; i < numsSize; i++) {
        int newIndex = abs(nums[i]) - 1;
        if (nums[newIndex] > 0) {
            nums[newIndex] *= -1;
        }
    }

    int *res = malloc(numsSize * sizeof(int));
    assert(res != NULL);
    int arrayIndex = 0;
    for (int i = 1; i <= numsSize; i++) {
        if (nums[i - 1] > 0) {
            res[arrayIndex++] = i;
        }
    }

    *returnSize = arrayIndex;

    res = realloc(res, arrayIndex * sizeof(int));

    return res;
}
