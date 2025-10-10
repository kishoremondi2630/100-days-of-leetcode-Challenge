class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m, n = len(word1), len(word2)
        
        # Use two rows to save space
        prev = [0] * (n + 1)
        curr = [0] * (n + 1)
        
        # Initialize first row
        for j in range(n + 1):
            prev[j] = j
        
        for i in range(1, m + 1):
            curr[0] = i  # Initialize first column of current row
            
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    curr[j] = prev[j - 1]
                else:
                    curr[j] = 1 + min(
                        prev[j],      # Delete
                        curr[j - 1],  # Insert
                        prev[j - 1]   # Replace
                    )
            
            # Move to next row
            prev, curr = curr, prev
        
        return prev[n]
