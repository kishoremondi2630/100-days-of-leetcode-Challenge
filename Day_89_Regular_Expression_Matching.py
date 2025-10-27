class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        memo = {}
        
        def dfs(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            
            # Base cases
            if j == len(p):
                return i == len(s)
            
            # Check if current character matches
            first_match = i < len(s) and (p[j] == '.' or p[j] == s[i])
            
            # Handle '*' case
            if j + 1 < len(p) and p[j + 1] == '*':
                # Zero occurrences OR one or more occurrences
                result = dfs(i, j + 2) or (first_match and dfs(i + 1, j))
            else:
                # Simple match and move forward
                result = first_match and dfs(i + 1, j + 1)
            
            memo[(i, j)] = result
            return result
        
        return dfs(0, 0)
