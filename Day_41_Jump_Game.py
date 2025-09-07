class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        max_reach = 0
        for i in range(n):
            if i > max_reach:
                return False
            if max_reach < i + nums[i]:
                max_reach = i + nums[i]
            if max_reach >= n - 1:
                return True
        return True
