class Solution:     # BFS
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        q = deque()

        for r in range(ROWS):
            if board[r][0] == 'O':
                q.append((r, 0))
                board[r][0] = 'T'  
            if board[r][COLS-1] == 'O':
                q.append((r, COLS-1))       
                board[r][COLS-1] = 'T' 
        for c in range(COLS):
            if board[0][c] == 'O':
                q.append((0,c))
                board[0][c] = 'T' 
            if board[ROWS-1][c] == 'O':
                q.append((ROWS-1,c))
                board[ROWS-1][c] = 'T' 


        while q:
            r, c = q.popleft()
            board[r][c] = 'T'
            for dr, dc in directions:
                new_r, new_c = r + dr, c + dc
                if new_r in range(ROWS) and new_c in range(COLS) and board[new_r][new_c] == 'O':
                    q.append((new_r,new_c))
                    board[new_r][new_c] = 'T'

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'T':
                    board[r][c] = 'O'
                elif board[r][c] == 'O':
                    board[r][c] = 'X'

