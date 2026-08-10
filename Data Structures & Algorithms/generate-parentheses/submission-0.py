class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        sub = []

        def dfs(opened, closed):
            if opened  == closed == n:
                res.append("".join(sub))
                return

            if opened < n:
                sub.append("(")
                dfs(opened + 1, closed)
                sub.pop()
            if closed < opened:
                sub.append(")")
                dfs(opened, closed + 1)
                sub.pop()

        dfs(0,0)
        return res   
