class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # Count frequency of each number
        freq_map = {}
        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1
        
        # Sort numbers by frequency in descending order
        sorted_nums = sorted(freq_map.keys(), key=lambda x: freq_map[x], reverse=True)
        
        # Return top k most frequent elements
        return sorted_nums[:k]
