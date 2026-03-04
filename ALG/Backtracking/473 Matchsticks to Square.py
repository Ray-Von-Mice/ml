class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        perimeter = sum(matchsticks)
        if perimeter % 4:
            return False
        
        boundary = perimeter // 4
        matchsticks.sort(reverse = True)
        edges = [0] * 4

        def dfs(indx):
            if indx == len(matchsticks):
                return True
            
            # making 4 edges by puting matchstick in
            for j in range(4):
                if edges[j] + matchsticks[indx] <= boundary:
                    edges[j] += matchsticks[indx]
                    if dfs(indx + 1):
                        return True
                    edges[j] -= matchsticks[indx]
                # pruning, after dfs and backtrack still 0, skip and return False
                if edges[j] == 0:
                    break
            
            return False
        
        return dfs(0)