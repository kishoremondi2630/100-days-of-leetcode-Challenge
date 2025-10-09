# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        # Min-heap to store (value, list_index, node)
        heap = []
        
        # Initialize heap with first node from each non-empty list
        for i, head in enumerate(lists):
            if head:
                heapq.heappush(heap, (head.val, i, head))
        
        # Dummy node to simplify list construction
        dummy = ListNode(0)
        current = dummy
        
        # Process nodes until heap is empty
        while heap:
            val, list_idx, node = heapq.heappop(heap)
            
            # Add current node to result list
            current.next = node
            current = current.next
            
            # If there's a next node in the same list, push it to heap
            if node.next:
                heapq.heappush(heap, (node.next.val, list_idx, node.next))
        
        return dummy.next
