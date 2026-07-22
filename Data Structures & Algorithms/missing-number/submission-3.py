class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)

        for i in range(len(nums)):
            res += i - nums[i]
        return res

# soluzione con somma, fa sum([0,n])-sum(nums) e viene fuori il numero mancante
# fa questa sottrazione volta x volta con i-nums[i]