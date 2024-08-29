# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        stack_a = ["A"]
        stack_b = ["B"]

        while headA or headB:
            if headA:
                stack_a.append(headA)
                headA = headA.next

            if headB:
                stack_b.append(headB)
                headB = headB.next

        prev = None
        while stack_a and stack_b:
            node_a = stack_a.pop()
            node_b = stack_b.pop()

            if node_a != node_b:
                return prev

            prev = node_a

        
