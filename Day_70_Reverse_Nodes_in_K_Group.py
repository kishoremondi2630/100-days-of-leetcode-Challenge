# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        # Count total nodes to handle edge cases
        count = 0
        current = head
        while current:
            count += 1
            current = current.next
        
        # If k is 1 or list is empty, no reversal needed
        if k <= 1 or not head:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        prev_group_end = dummy
        
        while count >= k:
            # Start of current group
            group_start = prev_group_end.next
            # End of current group (after reversal)
            group_end = group_start
            
            # Reverse k nodes
            prev = None
            current = group_start
            
            for _ in range(k):
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node
            
            # Connect the reversed group
            prev_group_end.next = prev  # prev is now the new head of reversed group
            group_end.next = current    # Connect to the next part
            
            # Move to next group
            prev_group_end = group_end
            count -= k
        
        return dummy.next
