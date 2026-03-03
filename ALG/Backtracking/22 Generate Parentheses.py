class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result, subset = [], []

        def dfs(lp_cnt, rp_cnt):
            # add left parenthesis when left < n
            # add right parenthesis when left > right
            # make result when left == right == n
            if lp_cnt > n or rp_cnt > n:
                return
            if lp_cnt == n and rp_cnt == n:
                string = "".join(subset[:])
                result.append(string)
                return
            
            if lp_cnt < n:
                subset.append("(")
                dfs(lp_cnt + 1, rp_cnt)
                subset.pop()
            if lp_cnt > rp_cnt: # DONT use elif, otherwise it would skip this section after dfs up returns
                subset.append(")")
                dfs(lp_cnt, rp_cnt + 1)
                subset.pop()
        
        dfs(0, 0)
        return result
            