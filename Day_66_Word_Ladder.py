class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if endWord not in wordList:
            return 0
        
        # Pre-process: create pattern dictionary
        pattern_dict = {}
        wordList.append(beginWord)
        
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + '*' + word[i+1:]
                if pattern not in pattern_dict:
                    pattern_dict[pattern] = []
                pattern_dict[pattern].append(word)
        
        # BFS with pattern matching
        queue = collections.deque([(beginWord, 1)])
        visited = {beginWord: True}
        
        while queue:
            current_word, level = queue.popleft()
            
            for i in range(len(current_word)):
                pattern = current_word[:i] + '*' + current_word[i+1:]
                
                if pattern in pattern_dict:
                    for neighbor in pattern_dict[pattern]:
                        if neighbor == endWord:
                            return level + 1
                        
                        if neighbor not in visited:
                            visited[neighbor] = True
                            queue.append((neighbor, level + 1))
                    
                    # Clear to avoid reprocessing
                    pattern_dict[pattern] = []
        
        return 0
