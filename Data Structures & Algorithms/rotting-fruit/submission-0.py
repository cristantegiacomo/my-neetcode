class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        q = deque()
        fresh = time = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)] 

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))

        while fresh > 0 and q:
            length = len(q)
            for i in range(length):
                r, c = q.popleft()

                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if 0 <= row < m and 0 <= col < n and grid[row][col] == 1:
                        grid[row][col] = 2
                        q.append((row, col))
                        fresh -= 1
            time += 1

        return time if fresh == 0 else -1    