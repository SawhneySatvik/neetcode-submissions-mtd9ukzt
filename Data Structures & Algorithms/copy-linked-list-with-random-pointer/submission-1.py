"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head

        hash_table = {}
        temp = head

        while temp:
            hash_table[temp] = Node(temp.val)
            temp = temp.next
        
        temp = head
        while temp:
            hash_table[temp].next = hash_table.get(temp.next)
            hash_table[temp].random = hash_table.get(temp.random)
            temp = temp.next
        
        return hash_table[head]