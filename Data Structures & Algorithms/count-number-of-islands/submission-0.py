class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        seen = set()
        cnt = 0

        def dfs(j, i):
            if j >= m or j < 0 or i >= n or i < 0:
                return 0

            if grid[j][i] == "0":
                return 0
                
            if (j, i) in seen:
                return 0
            
            seen.add((j, i))
            res =( dfs(j, i+1) +  #dx
                   dfs(j, i-1) +  #sx
                   dfs(j+1, i) +   #up
                   dfs(j-1, i) ) #down
            return 1 + res

        for j in range(m):
            for i in range(n):
                if grid[j][i] == "1" and (j,i) not in seen:
                    dfs(j,i)
                    cnt += 1
        return cnt
