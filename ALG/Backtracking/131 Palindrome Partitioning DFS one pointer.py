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
        n = len(s)
        def dfs(indx):
            if indx == len(s):
                result.append(subset[:])
                return
            
            for right in range(indx, n):
                cur_string = s[indx : right + 1]
                if self.isPalindrome(cur_string):
                    subset.append(cur_string)
                    # start dfs from next position "abc": "a" -> "b" .. or "ab" -> "c"
                    dfs(right + 1)
                    subset.pop()

        dfs(0)
        return result