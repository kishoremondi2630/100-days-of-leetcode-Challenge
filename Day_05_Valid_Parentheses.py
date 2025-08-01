class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            if char in mapping:
                top_element = stack.pop() if stack else '#' # If it's a closing bracket
                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char) # for an opening bracket

        return not stack # If stack is empty, all brackets were matched properly
