int max(int a, int b);

int findLengthOfLCIS(int* nums, int numsSize) {
    int lcis = 0, anchor = 0;

    for (int i = 0; i < numsSize; i++) {
        if (i && nums[i - 1] >= nums[i]) {
            anchor = i;
        }

        lcis = max(lcis, i - anchor + 1);
    }

    return lcis;
}

int max(int a, int b) {
    if (a > b) {
        return a;
    }

    return b;
}
