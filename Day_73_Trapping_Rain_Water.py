class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0
        
        left, right = 0, len(height) - 1
        left_max = right_max = trapped_water = 0
        
        while left < right:
            left_val, right_val = height[left], height[right]
            
            if left_val < right_val:
                if left_val >= left_max:
                    left_max = left_val
                else:
                    trapped_water += left_max - left_val
                left += 1
            else:
                if right_val >= right_max:
                    right_max = right_val
                else:
                    trapped_water += right_max - right_val
                right -= 1
        
        return trapped_water
