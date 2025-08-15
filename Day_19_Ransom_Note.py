class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        from collections import defaultdict

        # Create a frequency dictionary for the magazine
        magazine_counts = defaultdict(int)
        for char in magazine:
            magazine_counts[char] += 1
            
        # Check each character in the ransomNote
        for char in ransomNote:
            if magazine_counts[char] <= 0:
                return False
            magazine_counts[char] -= 1
        
        return True
