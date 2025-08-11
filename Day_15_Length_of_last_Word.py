class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Trim the trailing spaces
        trimmed = s.rstrip()
        length = 0
        # Iterate from the end of the trimmed string to find the last word's length
        for i in range(len(trimmed) - 1, -1, -1):
            if trimmed[i] == ' ':
                break
            length += 1
        return length
