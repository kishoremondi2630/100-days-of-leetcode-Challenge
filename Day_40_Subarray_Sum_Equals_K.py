class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        prefix_sum = 0
        sum_counts = {0: 1}  # Use regular dict instead of defaultdict

        for num in nums:
            prefix_sum += num
            # Check if (prefix_sum - k) exists in the dictionary
            if (prefix_sum - k) in sum_counts:
                count += sum_counts[prefix_sum - k]
            
            # Update the count for current prefix sum
            if prefix_sum in sum_counts:
                sum_counts[prefix_sum] += 1
            else:
                sum_counts[prefix_sum] = 1

        return count
