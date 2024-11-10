# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        linked_list = []

        while head:
            linked_list.append(head.val)
            head = head.next
        
        l = 0
        r = len(linked_list) - 1

        while l < r:
            if linked_list[l] != linked_list[r]:
                return False

            l += 1
            r -= 1
        
        return True

        
