class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        xorr = n
        for i in range(n):
            xorr ^= i ^ nums[i]
        return xorr


'''soluzione con xor:
A^A=0; A^0=A; Quindi qui fai lo xor tra tutti i numeri tra [0,N] e tutti i numeri in nums
ottieni 1^1^2^2^3^3^4 = 0^4 = 4
 '''