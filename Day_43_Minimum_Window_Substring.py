class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not s or not t or len(s) < len(t):
            return ""
        
        # Since there are 128 ASCII characters
        target = [0] * 128
        for char in t:
            target[ord(char)] += 1
        
        required = len(t)
        left = 0
        min_len = float('inf')
        min_left = 0
        
        for right in range(len(s)):
            # Expand the window by including the character at right
            char_right = s[right]
            if target[ord(char_right)] > 0:
                required -= 1
            target[ord(char_right)] -= 1
            
            # When the window has all required characters, try to contract from the left
            while required == 0:
                # Update the minimum window
                current_len = right - left + 1
                if current_len < min_len:
                    min_len = current_len
                    min_left = left
                
                # Remove the left character from the window
                char_left = s[left]
                target[ord(char_left)] += 1
                if target[ord(char_left)] > 0:
                    required += 1
                left += 1
        
        return "" if min_len == float('inf') else s[min_left:min_left + min_len]
