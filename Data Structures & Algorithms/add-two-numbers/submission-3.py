# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        temp1, temp2, temp = l1, l2, dummy
        carry = 0

        while temp1 or temp2 or carry:
            val1 = temp1.val if temp1 else 0
            val2 = temp2.val if temp2 else 0

            curr = val1 + val2 + carry
            carry = curr // 10
            curr %= 10

            temp.next = ListNode(curr)
            temp = temp.next

            if temp1:
                temp1 = temp1.next
            if temp2:
                temp2 = temp2.next

        return dummy.next
        