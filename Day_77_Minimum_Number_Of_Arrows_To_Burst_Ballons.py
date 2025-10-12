class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if not points:
            return 0
        
        # In-place sort and single variable tracking
        points.sort(key=lambda x: x[1])
        
        arrows = 1
        current_end = points[0][1]
        
        for i in range(1, len(points)):
            if points[i][0] > current_end:
                arrows += 1
                current_end = points[i][1]
        
        return arrows
