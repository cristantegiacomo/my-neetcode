class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = [0] * 26
        for task in tasks:
            count[ord(task) - ord('A')] += 1

        maxf = max(count)
        maxCount = 0
        for i in count:
            maxCount += 1 if i == maxf else 0

        time = (maxf - 1) * (n + 1) + maxCount
        return max(len(tasks), time)

    # soluzione matematica: se hai 4 A, 4 B, 2 C    n = 2
    # A _ _ A _ _ A _ _     3 blocchi: maxf-1=4-1=3
    # n+1=3 è la grandezza di ogni blocco (incluso A)
    # maxCount=2 perche A e B hanno freq=4
    # quindi: A B _ A B _ A B _ (A B) --> +2