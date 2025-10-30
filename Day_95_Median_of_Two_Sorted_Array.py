class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # Ensure nums1 is the smaller array for optimization
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        total_len = m + n
        half_len = (total_len + 1) // 2
        
        # Binary search on the smaller array
        left, right = 0, m
        
        while left <= right:
            # Partition nums1
            i = (left + right) // 2
            # Partition nums2 - j is calculated to make left half size = half_len
            j = half_len - i
            
            # Handle edge cases for boundaries
            nums1_left_max = float('-inf') if i == 0 else nums1[i - 1]
            nums1_right_min = float('inf') if i == m else nums1[i]
            
            nums2_left_max = float('-inf') if j == 0 else nums2[j - 1]
            nums2_right_min = float('inf') if j == n else nums2[j]
            
            # Check if we found the correct partition
            if nums1_left_max <= nums2_right_min and nums2_left_max <= nums1_right_min:
                # Found the correct partition
                if total_len % 2 == 1:
                    # Odd total length - median is max of left half
                    return max(nums1_left_max, nums2_left_max)
                else:
                    # Even total length - median is average of max(left) and min(right)
                    return (max(nums1_left_max, nums2_left_max) + 
                           min(nums1_right_min, nums2_right_min)) / 2.0
            elif nums1_left_max > nums2_right_min:
                # nums1's left half is too big, move partition left
                right = i - 1
            else:
                # nums1's left half is too small, move partition right
                left = i + 1
        
        # Should never reach here for valid inputs
        return 0.0
