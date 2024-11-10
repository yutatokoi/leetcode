class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            l_num, r_num = numbers[l], numbers[r]

            if l_num + r_num == target:
                return [l + 1, r + 1]
            elif l_num + r_num > target:
                r -= 1
            elif l_num + r_num < target:
                l += 1

        
