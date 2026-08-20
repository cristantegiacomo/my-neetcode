class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        
        maxf = max(max(seats), max(students))
        seatsBucket = [0] * (maxf + 1) # i
        studsBucket = [0] * (maxf + 1) # j
        i = j = 1
        res = 0

        for s in seats:
            seatsBucket[s] += 1
        for s in students:
            studsBucket[s] += 1
        

        while i < maxf + 1 and j < maxf + 1:

            while i < maxf+1 and seatsBucket[i] == 0:
                i += 1
            while j < maxf+1 and studsBucket[j] == 0:
                j += 1

            if i < maxf+1 and j < maxf+1:
                res += abs(i - j)
                seatsBucket[i] -= 1
                studsBucket[j] -= 1
        
        return res