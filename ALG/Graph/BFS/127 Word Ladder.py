class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0
        
        # Initialize queue for BFS: (current_word, current_distance)
        queue = deque([(beginWord, 1)])
        
        while queue:
            word, dist = queue.popleft()
            
            if word == endWord:
                return dist
            
            # Try changing every character position
            for i in range(len(word)):
                original_char = word[i]
                
                # Try every letter from 'a' to 'z'
                for char_code in range(ord('a'), ord('z') + 1):
                    new_char = chr(char_code)
                    if new_char == original_char:
                        continue
                    
                    # Construct the new word
                    new_word = word[:i] + new_char + word[i+1:]
                    
                    if new_word in wordSet:
                        queue.append((new_word, dist + 1))
                        # Remove from set to prevent visiting the same word twice
                        wordSet.remove(new_word)
                        
        return 0