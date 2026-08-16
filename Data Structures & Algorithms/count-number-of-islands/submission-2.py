class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        cnt = 0

        def dfs(j, i):
            if j >= m or j < 0 or i >= n or i < 0:
                return

            if grid[j][i] == "0" or grid[j][i] == "#":
                return
            
            grid[j][i] = "#"
            dfs(j, i+1)  #dx
            dfs(j, i-1)  #sx
            dfs(j+1, i)  #up
            dfs(j-1, i)  #down1


        for j in range(m):
            for i in range(n):
                if grid[j][i] == "1":
                    dfs(j,i)
                    cnt += 1
        return cnt
