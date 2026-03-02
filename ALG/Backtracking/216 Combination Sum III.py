class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result, subset = [], []

        def dfs(cur, total):
            if total == 0 and len(subset) == k:
                result.append(subset[:])
                return
            
            if len(subset) == k or total < 0:
                return
            
            # i is 0 based, but in problem description, k numbers are formed 1 based(1 ... 9)
            for i in range(cur, 9):
                subset.append(i + 1)
                dfs(i + 1, total - i - 1)
                subset.pop()
        
        dfs(0, n)
        return result