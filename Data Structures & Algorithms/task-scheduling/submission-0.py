class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-freq for freq in count.values()]
        heapq.heapify(maxHeap)

        time = 0
        q = deque()  # pairs of [-freq, idleTime]
        while maxHeap or q:
            time += 1

            if not maxHeap: #esempio: q=[-3,7] maxHeap vuoto prima time=6 ora time=7, time = 7 = q[0][1] = 7 resta invariato
                time = q[0][1] # al posto di fare while time==q[0][1]: time+=1
            else:
                freq = 1 + heapq.heappop(maxHeap)
                if freq < 0:
                    q.append([freq, time + n])

            if q and q[0][1] == time:   # il push lo faccio subito dopo q.append per considerare il caso in cui n = 0
                heapq.heappush(maxHeap, q.popleft()[0])

        return time