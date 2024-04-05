# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = l1
        curr2 = l2

        number1 = 0
        number2 = 0

        digit = 0

        while curr1 and curr2:
            number1 += curr1.val * (10 ** digit)
            number2 += curr2.val * (10 ** digit)
            curr1 = curr1.next
            curr2 = curr2.next
            digit += 1

        if curr1:
            while curr1:
                number1 += curr1.val * (10 ** digit)
                curr1 = curr1.next
                digit += 1
        elif curr2:
            while curr2:
                number2 += curr2.val * (10 ** digit)
                curr2 = curr2.next
                digit += 1

        number1 = str(number1)
        number2 = str(number2)

        result_num = int(number1[::-1]) + int(number2[::-1])
        result_digits = list(str(result_num))
        result_digits = result_digits[::-1]

        return result_digits

