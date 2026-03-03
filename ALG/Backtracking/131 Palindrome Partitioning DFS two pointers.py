class Solution:
    def isPalindrome(self, word: str) -> bool:
        left, right = 0, len(word) - 1
        while left < right:
            if word[left] != word[right]:
                return False
            left += 1
            right -= 1
        return True
     
    def partition(self, s: str) -> List[List[str]]:
        result, subset = [], []

        def dfs(start, end):
            if end == len(s):
                if start == end:
                    result.append(subset[:])
                return
            
            cur_string = s[start : end + 1]
            if self.isPalindrome(cur_string):
                subset.append(cur_string)
                dfs(end + 1, end + 1)
                subset.pop()
            
            dfs(start, end + 1)

        dfs(0, 0)
        return result