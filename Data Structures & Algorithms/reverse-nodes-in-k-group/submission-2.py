# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseLinkedList(self, start: Optional[ListNode], end: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = end, start
        while curr != end:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
    
    def getKthNode(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        while head and k > 0:
            head = head.next
            k -= 1
        return head

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        curr = dummy

        while True:
            kthNode = self.getKthNode(curr, k)
            if not kthNode:
                break
            
            nextNode = kthNode.next
            start = curr.next

            newList = self.reverseLinkedList(start, nextNode)

            curr.next = newList
            curr = start
        
        return dummy.next
            
