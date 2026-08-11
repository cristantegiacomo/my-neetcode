class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        res = []
        sub = []
        j = 0
        mp = {  
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl", 
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }


        def dfs(j):
            if j >= len(digits):
                res.append("".join(sub))
                return


            for char in mp[digits[j]]:
                sub.append(char)
                dfs(j+1)
                sub.pop()

        dfs(0)
        return res     