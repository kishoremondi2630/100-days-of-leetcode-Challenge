
###--- CHARACTER COUNT APPROACH---

from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        groups = defaultdict(list)
        for s in strs:
            count = [0] * 26  # For lowercase English letters
            for c in s:
                count[ord(c) - ord('a')] += 1
            groups[tuple(count)].append(s)  # Tuple is hashable
        return list(groups.values())      from collections import defaultdict


###---SORTING APPROACH---

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        groups = defaultdict(list)
        for s in strs:
            # For short strings, sorting can be faster than counting
            key = ''.join(sorted(s))
            groups[key].append(s)
        return list(groups.values())
