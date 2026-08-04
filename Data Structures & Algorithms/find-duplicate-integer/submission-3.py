class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
       # nums[i]: next
       # i: nodo attuale
       # sappiamo che si verifica sempre perforza il loop 
       # e l'inizio del loop è proprio i

# [1,2,3,2,2]
# 0 -> 1 -> 2 <-> 3     l'indice 2 viene puntato da MAX 2 frecce

# [1,2,3,1,4]
# 0 -> 1 -> 2 -> 3 -> 1 -> 2 -> 3 -> 1
# l'indice 1 viene puntato sempre da MAX 2 frecce

# [3,3,3,1,3]
# 0 -> 3 <-> 1

# spiegazione: se 3 duplicato, all'indice 3 punteranno almeno 2 elementi --> si verifica loop. Non si puo verificare loop per indice 0

        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        slow2 = 0
        while True:
            slow2 = nums[slow2]
            slow = nums[slow]
            if slow == slow2:
                return slow


