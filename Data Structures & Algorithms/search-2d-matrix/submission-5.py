class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n=len(matrix[0])

        l1, r1 = 0, len(matrix)-1

        while l1 <= r1:
            m1 = l1 + ((r1-l1) // 2)

            if matrix[m1][n-1] < target:
                l1 = m1 + 1
            elif matrix[m1][0] > target:
                r1 = m1 - 1
            else:
                l, r = 0, n-1
                while l <= r:
                    m = l + ((r-l) // 2)

                    if matrix[m1][m] < target:
                        l = m +1
                    elif matrix[m1][m] > target:
                        r = m - 1
                    else:
                        return True
                return False
        return False

#[[1,2,4,8],[10,11,12,13],[14,20,30,40],[45,48,50,60]]