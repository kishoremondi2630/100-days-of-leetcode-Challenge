class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        num_set = set(nums)
        max_len = 0
        
        for num in num_set:
            # Only process if it's the start of a sequence
            if num - 1 not in num_set:
                current_len = 1
                next_num = num + 1
                
                # Use while loop for minimal operations
                while next_num in num_set:
                    current_len += 1
                    next_num += 1
                
                if current_len > max_len:
                    max_len = current_len
        
        return max_len
