# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return head
        
        slow = fast = head

        for _ in range(n):
            if fast:
                fast = fast.next
            else:
                return head
        
        if not fast:
            return head.next
        
        prev = None
        while fast:
            prev = slow
            slow = slow.next
            fast = fast.next
        
        prev.next = prev.next.next if prev.next else None
        return head