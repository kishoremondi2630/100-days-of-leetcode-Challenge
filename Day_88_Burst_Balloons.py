class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        balloons = [1] + nums + [1]
        
        # Use 1D DP with careful indexing
        dp = [[0] * (n + 2) for _ in range(n + 2)]
        
        for length in range(1, n + 1):
            for left in range(0, n - length + 1):
                right = left + length + 1
                # Try each possible last balloon to burst
                for last in range(left + 1, right):
                    current = (balloons[left] * balloons[last] * balloons[right] +
                              dp[left][last] + dp[last][right])
                    if current > dp[left][right]:
                        dp[left][right] = current
        
        return dp[0][n + 1]
