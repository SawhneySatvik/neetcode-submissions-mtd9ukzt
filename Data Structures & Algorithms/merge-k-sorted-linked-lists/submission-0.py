class Solution:
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode(0)
        curr = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        
        curr.next = list1 if list1 else list2

        return dummy.next
    

    def mergeSort(self, lists, start, end):
        if start == end:
            return lists[start]
        
        mid = (start + end) // 2
        
        left = self.mergeSort(lists, start, mid)
        right = self.mergeSort(lists, mid + 1, end)
        
        return self.mergeTwoLists(left, right)
        

    def mergeKLists(self, lists):
        if not lists:
            return None
        
        return self.mergeSort(lists, 0, len(lists) - 1)
