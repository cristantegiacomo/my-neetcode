class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])

        def dfs(i, j, sett, idx):
            if idx == len(word):
                return True

            if i >= n or i < 0 or j >= m or j < 0:
                return False

            if (i,j) in sett:
                return False

            if board[j][i] != word[idx]:
                return False

            sett.add((i,j))
            dx = dfs(i+1, j, sett, idx+1) # destra
            sx = dfs(i-1, j, sett, idx+1) # sinistra
            up = dfs(i, j+1, sett, idx+1) # up
            down = dfs(i, j-1, sett, idx+1) # down
            sett.remove((i,j))
            return dx or sx or up or down
        
        var = False
        for j in range(m):
            for i in range(n):
                var = var or dfs(i, j, set(), 0)
        return var