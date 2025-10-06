import heapq

class MedianFinder(object):

    def __init__(self):
        self.small = []  # max heap
        self.large = []  # min heap
        # Pre-allocate to avoid dynamic resizing
        heapq.heapify(self.small)
        heapq.heapify(self.large)

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        # Optimized insertion logic
        if not self.small or num <= -self.small[0]:
            heapq.heappush(self.small, -num)
            if len(self.small) > len(self.large) + 1:
                heapq.heappush(self.large, -heapq.heappop(self.small))
        else:
            heapq.heappush(self.large, num)
            if len(self.large) > len(self.small):
                heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self):
        """
        :rtype: float
        """
        # Direct access without function calls for speed
        if len(self.small) == len(self.large):
            return (-self.small[0] + self.large[0]) * 0.5
        return -self.small[0] * 1.0
