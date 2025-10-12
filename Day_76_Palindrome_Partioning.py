class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        n = len(s)
        
        # Precompute palindrome information using dynamic programming
        is_palindrome = [[False] * n for _ in range(n)]
        
        # All single characters are palindromes
        for i in range(n):
            is_palindrome[i][i] = True
        
        # Check for palindromes of length 2
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                is_palindrome[i][i + 1] = True
        
        # Check for palindromes of length > 2
        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j] and is_palindrome[i + 1][j - 1]:
                    is_palindrome[i][j] = True
        
        def backtrack(start, current_partition):
            if start == n:
                result.append(current_partition[:])
                return
            
            for end in range(start, n):
                if is_palindrome[start][end]:
                    current_partition.append(s[start:end + 1])
                    backtrack(end + 1, current_partition)
                    current_partition.pop()
        
        result = []
        backtrack(0, [])
        return result
