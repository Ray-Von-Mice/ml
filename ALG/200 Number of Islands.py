class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        rows, cols = len(grid), len(grid[0])
        islandNum = 0

        def helper(r, c):
            visiting = deque()
            visiting.append((r, c))
            grid[r][c] = "x"

            while visiting:
                vp = visiting.popleft()
                for dir in directions:
                    vpr = vp[0] + dir[0]
                    vpc = vp[1] + dir[1]

                    # out of boundries or visited or water
                    if (vpr < 0 or vpr >= rows or vpc < 0 or vpc >= cols or grid[vpr][vpc] == "x"
                    or grid[vpr][vpc] == "0"):
                        continue

                    visiting.append((vpr, vpc))
                    grid[vpr][vpc] = "x"

        for gr in range(rows):
            for gc in range(cols):
                if grid[gr][gc] == "1":
                    helper(gr, gc)
                    islandNum += 1
    
        return islandNum