class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        len_haystack = len(haystack)
        len_needle = len(needle)
        if len_needle > len_haystack:
            return -1
        for i in range(len_haystack - len_needle + 1):
            if haystack[i:i+len_needle] == needle:
                return i
        return -1
