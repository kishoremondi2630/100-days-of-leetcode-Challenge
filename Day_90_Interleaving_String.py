class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        m, n, l = len(s1), len(s2), len(s3)
        
        # Multiple early termination checks
        if m + n != l:
            return False
        
        # Quick character check without Counter
        if sorted(s1 + s2) != sorted(s3):
            return False
        
        # Use the shorter string for DP to minimize space
        if m < n:
            return self.isInterleave(s2, s1, s3)
        
        # Ultra-optimized 1D DP
        dp = [False] * (n + 1)
        dp[0] = True
        
        # Initialize first row
        for j in range(1, n + 1):
            dp[j] = dp[j-1] and (s2[j-1] == s3[j-1])
            if not dp[j]:  # Early break if prefix fails
                break
        
        # Fill DP table with minimal operations
        for i in range(1, m + 1):
            # Update first column
            new_dp = [False] * (n + 1)
            new_dp[0] = dp[0] and (s1[i-1] == s3[i-1])
            
            for j in range(1, n + 1):
                idx = i + j - 1
                # Check both possibilities with short-circuit evaluation
                new_dp[j] = (dp[j] and s1[i-1] == s3[idx]) or \
                           (new_dp[j-1] and s2[j-1] == s3[idx])
            
            dp = new_dp
        
        return dp[n]
