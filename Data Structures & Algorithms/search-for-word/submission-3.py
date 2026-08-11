class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        sett = set()

        def dfs(i, j, idx):
            if idx == len(word):
                return True

            if i >= n or i < 0 or j >= m or j < 0:
                return False

            if (i,j) in sett:
                return False

            if board[j][i] != word[idx]:
                return False

            sett.add((i,j))
            res = (dfs(i+1, j, idx+1) or 
                   dfs(i-1, j, idx+1) or 
                   dfs(i, j+1, idx+1) or 
                   dfs(i, j-1, idx+1))
            sett.remove((i,j))
            return res
        
        for j in range(m):
            for i in range(n):
                if dfs(i, j, 0):
                    return True
        return False