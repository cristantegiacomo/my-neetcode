class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        m = len(heights)
        n = len(heights[0])
        res = []
        seen = set()

        def dfs(r, c, height):
            nonlocal pac, atl
            if not 0 <= r < m or not 0 <= c < n:
                return
            
            if heights[r][c] > height or (r,c) in seen:
                return
            
            if r == 0 or c == 0:
                pac = True

            if r == m-1 or c == n-1:
                atl = True
                
            if pac and atl:
                return

            seen.add((r,c))

            dfs(r, c+1, heights[r][c]) #dx
            dfs(r, c-1, heights[r][c]) #sx
            dfs(r+1, c, heights[r][c]) #up
            dfs(r-1, c, heights[r][c]) #down




        for r in range(m):
            for c in range(n):
                pac = atl = False
                seen.clear()
                dfs(r, c, float('inf'))
                if pac and atl:
                    res.append((r,c))

        return res