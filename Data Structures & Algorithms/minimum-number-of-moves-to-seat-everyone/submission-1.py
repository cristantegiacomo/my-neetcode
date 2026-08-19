class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        
        seats.sort()
        students.sort()
        cnt = 0

        for chair, stud in zip(seats, students):
            cnt += abs(chair - stud)

        return cnt