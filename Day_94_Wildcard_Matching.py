class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # Compress consecutive '*' in pattern
        compressed = []
        for char in p:
            if char == '*' and compressed and compressed[-1] == '*':
                continue
            compressed.append(char)
        p = ''.join(compressed)
        
        i, j = 0, 0
        star_idx = -1
        s_match = 0
        
        while i < len(s):
            if j < len(p) and (p[j] == '?' or p[j] == s[i]):
                # Direct match
                i += 1
                j += 1
            elif j < len(p) and p[j] == '*':
                # Found '*', remember positions
                star_idx = j
                s_match = i
                j += 1
            elif star_idx != -1:
                # Backtrack to last '*' and try matching one more character
                j = star_idx + 1
                s_match += 1
                i = s_match
            else:
                return False
        
        # Check remaining pattern characters
        while j < len(p) and p[j] == '*':
            j += 1
        
        return j == len(p)
