class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        result, subset = [], []
        sdict = set(wordDict)

        def dfs(indx):
            if indx >= len(s):
                solution = " ".join(subset)
                result.append(solution)
                return
            
            for i in range(indx, len(s)):
                cur_word = s[indx: i + 1]
                if cur_word in wordDict:
                    subset.append(cur_word)
                    dfs(i + 1)
                    subset.pop()
        
        dfs(0)
        return result