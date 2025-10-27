import heapq

class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        if not buildings:
            return []
        
        # Pre-allocate events array for maximum speed
        n = len(buildings)
        events = [None] * (2 * n)
        
        # Build events array manually (faster than append)
        for i in range(n):
            l, r, h = buildings[i]
            events[2*i] = (l, -h, r)    # start event
            events[2*i + 1] = (r, 0, 0) # end event
        
        # In-place sort with custom key (faster than lambda)
        events.sort()
        
        # Initialize with sentinel values
        res = []
        heap = [(-0, float('inf'))]  # (negative_height, right)
        prev_height = 0
        
        for x, neg_h, r in events:
            # Lazy deletion from heap
            while heap[0][1] <= x:
                heapq.heappop(heap)
            
            # Add new building if start event
            if neg_h < 0:
                heapq.heappush(heap, (neg_h, r))
            
            # Check if height changed
            current_height = -heap[0][0]
            if current_height != prev_height:
                res.append([x, current_height])
                prev_height = current_height
        
        return res
