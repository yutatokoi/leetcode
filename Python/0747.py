class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        largest = -1
        second_largest = -2
        answer = -1

        for i in range(len(nums)):
            if nums[i] >= largest:
                second_largest = largest
                largest = nums[i]
                answer = i
            elif nums[i] > second_largest and nums[i] < largest:
                second_largest = nums[i]

        print(second_largest)
        print(largest)
        print(answer)

        if largest < (second_largest * 2):
            return -1

        return answer
