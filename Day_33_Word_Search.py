class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def dfs(i, j, index):
            if index == len(word):
                return True
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[index]:
                return False
            temp = board[i][j]
            board[i][j] = '#'
            found = dfs(i+1, j, index+1) or dfs(i-1, j, index+1) or dfs(i, j+1, index+1) or dfs(i, j-1, index+1)
            board[i][j] = temp
            return found
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0):
                    return True
        return False

###---MORE OPTIMISED CODE---
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        m, n = len(board), len(board[0])
        # If the word is longer than the total number of cells, return false
        if len(word) > m * n:
            return False
        
        # Frequency check: if the board doesn't have enough of a character, return false
        from collections import Counter
        board_freq = Counter()
        for row in board:
            board_freq.update(row)
        word_freq = Counter(word)
        for char in word_freq:
            if word_freq[char] > board_freq[char]:
                return False
        
        # Reverse the word if the last character is less common than the first
        if board_freq[word[0]] > board_freq[word[-1]]:
            word = word[::-1]
        
        def dfs(i, j, index):
            if index == len(word):
                return True
            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != word[index]:
                return False
            temp = board[i][j]
            board[i][j] = '#'
            found = (dfs(i+1, j, index+1) or
                     dfs(i-1, j, index+1) or
                     dfs(i, j+1, index+1) or
                     dfs(i, j-1, index+1))
            board[i][j] = temp
            return found
        
        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        return False
