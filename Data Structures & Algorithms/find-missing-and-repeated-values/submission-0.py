class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:

        n = len(grid)
        exp = n**2
        seen = set()
        ans = [-1, -1]
        
        for j in range(n):
            for i in range(n):
                if grid[j][i] not in seen:
                    seen.add(grid[j][i])
                else:
                    ans[0] = grid[j][i]
        
        for i in range(1, exp+1):
            if i not in seen:
                ans[1] = i

        return ans
