class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        m = len(heights)
        n = len(heights[0])
        res = []
        pacificSet = set()
        atlanticSet = set()

        def dfs(r, c, height, p):
            if not 0 <= r < m or not 0 <= c < n:
                return

            if heights[r][c] < height:
                return

            if p and (r,c) in pacificSet:
                return
            if not p and (r,c) in atlanticSet:
                return

            if p:
                pacificSet.add((r,c))
            else:
                atlanticSet.add((r,c))
            
            dfs(r, c+1, heights[r][c], p) #dx
            dfs(r, c-1, heights[r][c], p) #sx
            dfs(r+1, c, heights[r][c], p) #up
            dfs(r-1, c, heights[r][c], p) #down


        for c in range(n):
            dfs(0, c, 0, p=True)
            dfs(m-1, c, 0, p=False)
            
        for r in range(m):
            dfs(r, 0, 0, p=True)
            dfs(r, n-1, 0, p=False)


        for r, c in (pacificSet & atlanticSet):
                res.append([r,c])
        
        return res

    # soluzione ottimale O(m*n)