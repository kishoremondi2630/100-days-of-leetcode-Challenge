class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(intervals)<=1:
            return intervals
        intervals.sort(key=lambda x:x[0])
        result=[]
        new_interval=intervals[0]
        result.append(new_interval)
        for interval in intervals[1:]:
            if interval[0]<=new_interval[1]:
                new_interval[1]=max(new_interval[1],interval[1])
            else:
                new_interval=interval
                result.append(new_interval)
        return result
