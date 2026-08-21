class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        mapUnlock = defaultdict(list)
        indegree = [0] * numCourses

        for l, r in prerequisites:
            mapUnlock[r].append(l)
            indegree[l] += 1

        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        while q:
            course = q.popleft()
            res.append(course)
            for nbr in mapUnlock[course]:
                indegree[nbr] -= 1  
                if indegree[nbr] == 0:
                    q.append(nbr)

        return res if len(res) == numCourses else []     