class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        res = 0

        for i in range(len(logs)):
            if logs[i][0] == ".":
                if logs[i][1] == "." and stack:
                    stack.pop()
            else:
                stack.append(logs[i])

        while stack:
            stack.pop()
            res += 1
        return res