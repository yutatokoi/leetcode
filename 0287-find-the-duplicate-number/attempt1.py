class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        fast = 1
        length = len(nums)

        while slow != fast and nums[slow] != nums[fast]:
            if slow == length - 1:
                slow = 0
            else:
                slow += 1
            
            if fast == length - 1:
                fast = 1
            elif fast == length - 2:
                fast = 0
            else:
                fast += 2
        
        return nums[slow]

