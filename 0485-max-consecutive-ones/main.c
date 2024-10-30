int findMaxConsecutiveOnes(int* nums, int numsSize) {
    int max = 0, i = 0;
    while (i < numsSize) {
        int curr = 0;
        while (i < numsSize && nums[i] == 1) {
            if (++curr > max) max = curr;
            i++;
        }
        i++;
    }
    return max;
}
