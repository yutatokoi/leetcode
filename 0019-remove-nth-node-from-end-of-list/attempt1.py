# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Reverse initial list
        prev1 = None
        curr1 = head
        while curr1:
            nxt = curr1.next
            curr1.next = prev1
            prev1 = curr1
            curr1 = nxt
        
        # Remove the n-th from list
        m = 2
        prev2 = None
        curr2 = prev1
        while curr2:
            if m == n and curr2.next:
                nxt = curr2.next.next
                curr2.next = prev2
                prev2 = curr2
                curr2 = nxt
            else:
                nxt = curr2.next
                curr2.next = prev2
                prev2 = curr2
                curr2 = nxt
            m += 1

        return prev2

