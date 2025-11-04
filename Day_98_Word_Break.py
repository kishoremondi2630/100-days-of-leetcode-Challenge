class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        word_set = set(wordDict)
        n = len(s)
        
        # Group words by their starting character for faster lookup
        word_starts = {}
        for word in word_set:
            if word[0] not in word_starts:
                word_starts[word[0]] = []
            word_starts[word[0]].append(word)
        
        dp = [False] * (n + 1)
        dp[0] = True
        
        for i in range(n):
            if not dp[i]:
                continue
                
            # Only check words that start with current character
            current_char = s[i]
            if current_char in word_starts:
                for word in word_starts[current_char]:
                    end = i + len(word)
                    if end <= n and s[i:end] == word:
                        dp[end] = True
                        if end == n:
                            return True
        
        return dp[n]
