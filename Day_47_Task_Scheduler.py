class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        from collections import Counter
        
        freq = Counter(tasks)
        max_freq = max(freq.values())
        count_max = sum(1 for f in freq.values() if f == max_freq)
        
        min_intervals = (max_freq - 1) * (n + 1) + count_max
        return max(min_intervals, len(tasks))
