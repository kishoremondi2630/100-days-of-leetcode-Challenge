###---USING SET---
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_set = set()
        left = 0
        max_length = 0
        
        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            max_length = max(max_length, right - left + 1)
        
        return max_length

###---USING HASHMAP---
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_index = {}
        left = 0
        max_length = 0
        
        for right in range(len(s)):
            if s[right] in char_index:
                left = max(left, char_index[s[right]] + 1)
            char_index[s[right]] = right
            max_length = max(max_length, right - left + 1)
        
        return max_length
    
###---USING FIXED SIZE ARRAY---
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_index = [-1] * 128  # Assuming ASCII characters
        left = 0
        max_length = 0
        
        for right in range(len(s)):
            if char_index[ord(s[right])] >= left:
                left = char_index[ord(s[right])] + 1
            char_index[ord(s[right])] = right
            max_length = max(max_length, right - left + 1)
        
        return max_length
