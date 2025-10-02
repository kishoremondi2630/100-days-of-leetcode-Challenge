# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if not head or not head.next or not head.next.next:
            return
        
        # Step 1: Find middle in single pass
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        # Step 2: Reverse second half and merge in single operations
        # Reverse second half
        prev, curr = None, slow.next
        slow.next = None  # Split the list
        
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        # Step 3: Merge with minimal operations
        first, second = head, prev
        while second:
            first_next = first.next
            second_next = second.next
            
            first.next = second
            second.next = first_next
            
            first = first_next
            second = second_next
