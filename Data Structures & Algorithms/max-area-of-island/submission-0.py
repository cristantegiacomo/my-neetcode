class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        maxArea = 0

        def dfs(j,i):
            if j >= m or j < 0 or i >= n or i < 0:
                return 0
            
            if grid[j][i] != 1:
                return 0
            
            grid[j][i] = -1
            res = ( dfs(j, i+1) +   #dx
                    dfs(j, i-1) +   #sx
                    dfs(j+1, i) +   #up
                    dfs(j-1, i) )   #down
            return 1 + res

        for j in range(m):
            for i in range(n):
                if grid[j][i] == 1:
                    maxArea = max(maxArea, dfs(j,i))
        return maxArea