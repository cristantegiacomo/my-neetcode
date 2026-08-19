class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        mp = defaultdict(list)
        seen = set()
        for l, r in prerequisites:
            mp[l].append(r)

        def dfs(course):
            if course in seen:
                return False

            if len(mp[course]) == 0:
                return True

            seen.add(course)
            for nbr in mp[course]:
                if not dfs(nbr):
                    return False
                    
            seen.remove(course)
            mp[course].clear()
            return True


        for i in range(numCourses):
            if not dfs(i):
                return False
        return True