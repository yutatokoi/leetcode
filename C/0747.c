int dominantIndex(int* nums, int numsSize) {
    int largest = -1, second_largest = -1, answer = -1;

    for (int i = 0; i < numsSize; i++) {
        if (nums[i] >= largest) {
            second_largest = largest;
            largest = nums[i];
            answer = i;
        } else if (nums[i] < largest && nums[i] > second_largest) {
            second_largest = nums[i];
        }
    }

    if (largest < (second_largest * 2)) {
        return -1;
    }

    return answer;
}
