class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        setLock = set()
        mpLock = defaultdict(set)
        mpUnlock = defaultdict(list)
        seen = set()
        for l, r in prerequisites:
            mpUnlock[r].append(l)   # r può sbloccare l
            mpLock[l].add(r)     # l può essere sbloccato da r
            setLock.add(l)

        q = deque()
        for i in range(numCourses):
            if i not in setLock:
                q.append(i)
                seen.add(i)

        while q:
            course = q.popleft()
            res.append(course)

            for nbr in mpUnlock[course]:
                mpLock[nbr].remove(course)
                if nbr not in seen and not mpLock[nbr]:
                    q.append(nbr)
                    seen.add(nbr)

        return res if len(res) == numCourses else [] 