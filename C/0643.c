int max(int a, int b);

double findMaxAverage(int* nums, int numsSize, int k) {
    int curr_sum = 0;
    for (int i = 0; i < k; i++) {
        curr_sum += nums[i];
    }
    int max_sum = curr_sum;

    for (int i = k; i < numsSize; i++) {
        curr_sum += nums[i] - nums[i - k];
        max_sum = max(max_sum, curr_sum);
    }

    return max_sum / (double)k;
}

int max(int a, int b) {
    if (a > b) {
        return a;
    }

    return b;
}
