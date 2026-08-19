class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:

        cnt = 0
        
        for _ in range(len(seats)):
            cnt += abs(max(seats) - max(students))
            seats.remove(max(seats))
            students.remove(max(students))

        return cnt