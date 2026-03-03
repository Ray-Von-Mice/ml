class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mp = { '1' : [], '2' : ["a", "b", "c"], '3' : ["d", "e", "f"], '4' : ["g", "h", "i"], \
        '5' : ["j", "k", "l"], '6' : ["m", "n", "o"], '7' : ["p", "q", "r", "s"], '8' : ["t", "u", "v"], \
        '9' : ["w", "x", "y", "z"]}

        result, subset = [], []
        n = len(digits)
        def dfs(indx):
            if indx == n:
                result.append("".join(subset[:]))
                return
            
            arr = mp[digits[indx]]
            for i in range(len(arr)):
                subset.append(arr[i])
                dfs(indx + 1)
                subset.pop()

        dfs(0)
        return result